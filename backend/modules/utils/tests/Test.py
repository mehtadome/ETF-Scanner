import pandas as pd
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import functions as test_functions

# Basic usage
def main():
    try:
        # Basic DFs
        # test_etf_df()
        # test_mf_df()
        # test_haunted_df()

        # Advanced DFs
        print("The following is the combined dataframes")
        combined_data = test_functions.combine_sheets_data_safe()
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
