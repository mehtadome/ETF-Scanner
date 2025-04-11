from dotenv import load_dotenv
import pandas as pd
from functools import lru_cache

# My own modules
from ...utils.exports import init_table
from ...utils.clean import clean_ETFs
from ...utils.filters.filter import filter_etfs_with_ranges
from ..constants import COLUMNS_TO_CLEAN, LOGGER_BAR

# Cache the dataframe initialization
@lru_cache(maxsize=1)
def get_inited_etf_dataframe():
    df_etf = init_table.export_etf_loggerless()

    # Process the df once and store it. 
    #   Changes the values of '1 Yr Return' to floats.
    df_etf['1 Yr Return'] = df_etf['1 Yr Return'].apply(
        lambda x: float(x.replace('%', '')) if isinstance(x, str) and x != '--' else None
    )
    # print("ETFs Dataframe:\n\n\n", f"\n{df_etf.head(1)}\n\n\n")
    return df_etf 


# Cache the dataframe initialization
@lru_cache(maxsize=1)
def get_one_year_return(risk, expense, level, logger):
    # Init table
    logger.info(LOGGER_BAR)
    logger.info("Initializing combined sheets ETF dataframe.")
    df_etf = init_table.export_combined_sheets_loggerless()
    logger.info(f"\n {df_etf.head(10)}")

    # Clean table
    logger.info("\n\nCleaning combined sheets ETF dataframe.")
    df_etf = clean_ETFs.clean_percentage_columns(df_etf, COLUMNS_TO_CLEAN)
    logger.info(f"\n {df_etf.head(10)}")

    # Strip out every column but the ones we need
    logger.info("\n\nStripping unneeded columns from the ETF dataframe.")
    df_etf = df_etf[clean_ETFs.COLUMNS_TO_KEEP]
    logger.info(f"Remaining columns are: {df_etf.columns}")

    # **IMPORTANT**: For now, risk is hard-coded to stay at Low and Year return is hard-coded to 1.
    logger.info(f"\n\nFiltering ETFs based on risk={risk}, expense={expense}, and returnlevels={level}.")
    risk = "Low"
    filtered_df_etf, summary = filter_etfs_with_ranges(
        df_etf,
        risk_level=risk,
        expense_level=expense,
        return_level=level
    )

    # Log the summary
    logger.info("\n\nFilter Summary:\n")
    for key, value in summary.items():
        logger.info(f"{key}: {value}")
    
    # Dataframe in ['1 Yr Return'] descending order
    logger.info(f"\n\nETFs sorted by 1 Year Return in descending order is {filtered_df_etf.head(10)}.")

    return_dict = {
    name: {
        'return': ret,
        'expense': exp,
        'alpha': alpha
    }
        for name, ret, exp, alpha in zip(
            filtered_df_etf['ETF Name'],
            filtered_df_etf['1 Yr Return'],
            filtered_df_etf['Expense Ratio'],
            filtered_df_etf['3-Year Alpha']
        )
    }

    print(f"\n\nSize of dictionary is {len(return_dict)}")

    return return_dict
   

def etf_one_year_return():
    return_dict = {}

    # Lambda function to strip out null values and dashes
    # df_etf['1 Yr Return'] = df_etf['1 Yr Return'].apply(lambda x: 
    # float(x.replace('%', '')) if isinstance(x, str) and x != '--' else None)

    df_etf = get_inited_etf_dataframe()

    # Then get top 10
    df_top_10 = df_etf.nlargest(10, '1 Yr Return')[['ETF Name', '1 Yr Return']]

    # Pair vals such that dictionary is <ETF Name: 1 Yr Return>
    return_dict = dict(zip(df_top_10['ETF Name'], df_top_10['1 Yr Return']))
    print("Return dictionary", return_dict, "\n\nSize of dictionary is", len(return_dict))

    return return_dict