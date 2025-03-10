import os
from dotenv import load_dotenv
import pandas as pd
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))



# Load environment variables from .env file
load_dotenv()

etf_path = os.getenv('ETF_FILE_PATH')
mutual_fund_path = os.getenv('MUTUAL_FUNDS_FILE_PATH')
test_path = os.getenv('TEST_FILE_PATH')

# Basic usage
def main():
    print("Pandas version", pd.__version__)
    try:
        # Read the Excel file into a pandas DataFrame
        df_etf = pd.read_excel(etf_path,
                    sheet_name='Performance',
                    header=0,
                    index_col=0)

        # Convert the first 10 rows to a string and log it
        # print("ETFs Dataframe:\n\n\n", f"{df_etf.head(10)}")

        print("\n")
        print("ETFs columns are", df_etf.columns)
        print("ETFs Dataframe:", f"\n{df_etf.head(5)}\n\n\n")

        df_mutual_fund = pd.read_excel(mutual_fund_path,
                    sheet_name='Performance - Avg Annual Return',
                    index_col=0)
        
        print("\n")
        print("Mutual Funds columns are", df_etf.columns)
        print("Mutual Funds Dataframe:", f"\n{df_mutual_fund.head(5)}\n\n\n")
        #print("Mutual Funds Dataframe:", f"\n{df_mutual_fund.head(10)}")

        df_test = pd.read_excel(test_path,
                    sheet_name='Sheet1',
                    index_col=0)
        print("Haunted Dataframe:", f"\n{df_test.head(5)}\n\n\n")
        print("Haunted columns are", df_test.columns)

        df_test_2 = pd.read_excel(test_path,
                    sheet_name='totheright',
                    index_col=0)
        print("Haunted Dataframe:", f"\n{df_test_2.head(5)}\n\n\n")
        print("Haunted columns are", df_test_2.columns)


        # for i in df_test['1 Yr Return']:
        #     print("value is", i)



    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Starting Main Testing function\n-----------------------\n")
    print("The purpose of this file is to validate correct parsing the the XLS files.")
    main()
    print("\n-----------------------\nEnd of testing program")
