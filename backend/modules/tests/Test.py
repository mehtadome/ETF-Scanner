import os
from dotenv import load_dotenv
import pandas as pd
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))



# Load environment variables from .env file
load_dotenv()

etf_path = os.getenv('ETF_FILE_PATH')
mutual_fund_path = os.getenv('MUTUAL_FUNDS_FILE_PATH')
test_path = os.getenv('TEST_FILE_PATH')

def combine_sheets_data_safe():
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

def test_etf_df():
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


def test_mf_df():
    df_mutual_fund = pd.read_excel(mutual_fund_path,
                    sheet_name='Performance - Avg Annual Return',
                    index_col=0)
    print("\n")
    print("Mutual Funds columns are", df_mutual_fund.columns)
    print("Mutual Funds Dataframe:", f"\n{df_mutual_fund.head(5)}\n\n\n")
    #print("Mutual Funds Dataframe:", f"\n{df_mutual_fund.head(10)}")


def test_haunted_df():
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


# Basic usage
def main():
    try:
        # Basic DFs
        # test_etf_df()
        # test_mf_df()
        # test_haunted_df()

        # Advanced DFs
        print("The following is the combined dataframes")
        combined_data = combine_sheets_data_safe()
        combined_data.columns = combined_data.columns.str.strip()
        print(f"Combined column names are {combined_data.columns}\n")
        print(combined_data.head())
        # for i in df_test['1 Yr Return']:
        #     print("value is", i)



    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Starting Main Testing function\n-----------------------\n")
    print(f"The purpose of this file is to validate correct parsing the the XLS files.\nPandas version {pd.__version__}\n\n")
    main()
    print("\n-----------------------\nEnd of testing program")
