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
