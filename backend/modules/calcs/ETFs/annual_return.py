from dotenv import load_dotenv
import pandas as pd
from functools import lru_cache

# My own modules
from ...exports import init_table

# Load environment variables from .env file
load_dotenv()

# Cache the dataframe initialization
@lru_cache(maxsize=1)
def get_inited_etf_dataframe():
    df_etf = init_table.export_etf_loggerless()

    # Process the df once and store it
    df_etf['1 Yr Return'] = df_etf['1 Yr Return'].apply(
        lambda x: float(x.replace('%', '')) if isinstance(x, str) and x != '--' else None
    )
    # print("ETFs Dataframe:\n\n\n", f"\n{df_etf.head(1)}\n\n\n")

    return df_etf

# Can separate into own folder later
# df_mutual_fund = init_table.export_mutual_fund_loggerless()
#print("Mutual Funds Dataframe:", f"\n{df_mutual_fund.head(10)}")

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

# Write a function that gets the top 10 maxes
def top_10_max():
    # Sort the dataframe by 1 Yr Return in descending order
    df_sorted = df_etf.sort_values(by='1 Yr Return', ascending=False)
    # Get the top 10 rows
    top_10 = df_sorted.head(10)
    # Print the top 10 rows
    print(top_10)

#top_10_max()