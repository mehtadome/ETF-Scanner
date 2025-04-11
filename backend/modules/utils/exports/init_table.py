import os
# os.getenv('USERNAME')
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()

etf_path = os.getenv('ETF_FILE_PATH')
mutual_fund_path = os.getenv('MUTUAL_FUNDS_FILE_PATH')

# Basic usage
def export_etf(logger):
    """
    Export the dataframe tied to ETFs.
    
    Args:
        logger (app.logger): Application's logger.
    Returns:
        Pandas Dataframe.
    """
    logger.info(f"Received request for parsing ETF catolog")

    df_etf = pd.read_excel(etf_path,
                   sheet_name='Performance',
                   index_col=0)
    
    # Convert the first 10 rows to a string and log it
    logger.info("First 10 rows of ETF dataframe:")
    logger.info("\n" + f"\n{df_etf.head(10).to_dict()}")
    
    # print (df_etf)
    return df_etf


def export_mutual_fund(logger):
    """
    Export the dataframe tied to Mutual Funds.
    
    Args:
        logger (app.logger): Application's logger.
    Returns:
        Pandas Dataframe.
    """
    logger.info(f"Received request for parsing Mutual Funds catolog")

    df_mutual_fund = pd.read_excel('file-2.xls',
                   sheet_name='Performance - Avg Annual Return',
                   index_col=0)
    
    # Convert the first 10 rows to a string and log it
    logger.info("First 10 rows of Mutual Funds dataframe:")
    logger.info("\n" + f"\n{df_mutual_fund.head(10).to_dict()}")
    

    # print (df_mutual_fund)
    return df_mutual_fund


# LOGGERLESS FUNCTIONS
def export_combined_sheets_loggerless():
    """
    Safe function which combines the columns from three different sheets into one dataframe.
        * The sheets are 'Current Criteria', 'Performance', 'Risk'
    
    Returns:
        Pandas Dataframe.
    """
    try:
        # Read the Excel file
        excel_file = pd.ExcelFile(etf_path)

        # Verify all required sheets exist
        required_sheets = {'Current Criteria', 'Performance', 'Risk'}
        available_sheets = set(excel_file.sheet_names)

        if (required_sheets - available_sheets):
            raise ValueError(f"Missing sheets: {required_sheets - available_sheets}")
        
        # Read sheets with error handling
        dfs = {}
        for sheet in required_sheets:
            try:
                df = pd.read_excel(excel_file, sheet_name=sheet, index_col=0)
                if 'ETF Name' not in df.columns:
                    raise ValueError(f"Missing 'Name' column in sheet '{sheet}'")
                dfs[sheet] = df
            except Exception as e:
                raise ValueError(f"Error reading sheet '{sheet}': {e}")
            
        # Merge dataframes with validation
        result = dfs['Performance']
        for sheet in ['Current Criteria', 'Risk']:
            # Check for duplicate names before merging
            if dfs[sheet]['ETF Name'].duplicated().any():
                raise ValueError(f"Duplicate names found in sheet '{sheet}'")
            
            # Merge dataframes
            result = result.merge(
                dfs[sheet],
                on='ETF Name',
                how='inner',
                validate='one_to_one',
                indicator=True
            )

            # Check for unmatched rows
            unmatched = result[result['_merge'] != 'both']
            if not unmatched.empty:
                print(f"Warning: {len(unmatched)} unmatched rows present when merging {sheet}")

            result = result.drop(columns=['_merge'], axis=1)
        
        return result
    except Exception as e:
        print(f"Error processing Excel file: {str(e)}")
        raise


def export_etf_loggerless():
    """
    Export the dataframe tied to ETFs without requiring a logger to be passed.
    
    Returns:
        Pandas Dataframe.
    """
    df_etf = pd.read_excel(etf_path,
                   sheet_name='Performance',
                   index_col=0)
    # print (df_etf)
    return df_etf


def export_mutual_fund_loggerless():
    """
    Export the dataframe tied to Mutual Funds without requiring a logger to be passed..

    Returns:
        Pandas Dataframe.
    """

    df_mutual_fund = pd.read_excel(mutual_fund_path,
                   sheet_name='Performance - Avg Annual Return',
                   index_col=0)

    # print (df_mutual_fund)
    return df_mutual_fund


