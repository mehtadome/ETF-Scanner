from dotenv import load_dotenv
import pandas as pd
from functools import lru_cache

# My own modules
from ...utils.exports import init_table
from ...utils.clean import clean_ETFs
from ..constants import ETF_LEVELS

# Load environment variables from .env file
load_dotenv()

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

# Can separate into own folder later
# df_mutual_fund = init_table.export_mutual_fund_loggerless()
#print("Mutual Funds Dataframe:", f"\n{df_mutual_fund.head(10)}")

# Cache the dataframe initialization
@lru_cache(maxsize=1)
def get_inited_combined_etf_dataframe():
    # Init table
    df_etf = init_table.export_combined_sheets_loggerless()
    # Clean table
    df_etf = clean_ETFs.clean_percentage_columns(df_etf, clean_ETFs.COLUMNS_TO_CLEAN)

    # Strip out every column but the ones we need
    df_etf = df_etf[clean_ETFs.COLUMNS_TO_KEEP]

    return df_etf


# def get_risk_level(risk_level):
#     case = {
#         'low': ETF_LEVELS['low'],
#         'medium': ETF_LEVELS['medium'],
#         'high': ETF_LEVELS['high']
#     }

# def get_expense_level(expense_ratio):

# def get_return_level(return_ratio):


# Hard coded to 1 year return still
def best_etfs(risk_level, expense_ratio, return_ratio):
    df_etf = get_inited_combined_etf_dataframe()
    # Filter the dataframe based on each level




    

def one_year_return():
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

#one_year_return()