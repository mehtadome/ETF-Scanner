from dotenv import load_dotenv
import pandas as pd
from functools import lru_cache

# My own modules
from ...exports import init_table

# Load environment variables from .env file
load_dotenv()

# Cache the dataframe initialization
@lru_cache(maxsize=1)
def get_inited_mf_dataframe():
    df_mf = init_table.export_mutual_fund_loggerless()

    # Process the df once and store it. 
    #   Changes the values of 'Category Return 10 Yr Return' to floats and strips out dashes and nulls.
    df_mf['Category Return 10 Yr Return'] = df_mf['Category Return 10 Yr Return'].apply(
        lambda x: float(x.replace('%', '')) if isinstance(x, str) and x != '--' else None
    )
    # print("Mutual Funds Dataframe:\n\n\n", f"\n{df_mf.head(1)}\n\n\n")
    return df_mf

# Can separate into own folder later
# df_mutual_fund = init_table.export_mutual_fund_loggerless()
#print("Mutual Funds Dataframe:", f"\n{df_mutual_fund.head(10)}")

def one_year_return():
    return_dict = {}

    df_mf = get_inited_mf_dataframe()

    # Then get top 10
    df_top_10 = df_mf.nlargest(10, 'Category Return 10 Yr Return')[['Fund Name', 'Category Return 10 Yr Return']]

    # Pair vals such that dictionary is <Fund Name: Category Return 10 Yr Return>
    return_dict = dict(zip(df_top_10['Fund Name'], df_top_10['Category Return 10 Yr Return']))
    print("Return dictionary", return_dict, "\n\nSize of dictionary is", len(return_dict))

    return return_dict

#one_year_return()
