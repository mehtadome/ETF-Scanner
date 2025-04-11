"""
This file is intended for functions to test in main class Test.py
"""
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()

etf_path = os.getenv('ETF_FILE_PATH')
mutual_fund_path = os.getenv('MUTUAL_FUNDS_FILE_PATH')
test_path = os.getenv('TEST_FILE_PATH')

# INIT_TABLE
def export_combined_sheets_loggerless():
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


def export_mutual_fund_loggerless():
    """Test Mutual Fund dataframe initialization"""
    df_mutual_fund = pd.read_excel(mutual_fund_path,
                    sheet_name='Performance - Avg Annual Return',
                    index_col=0)
    print("\n")
    print("Mutual Funds columns are", df_mutual_fund.columns)
    print("Mutual Funds Dataframe:", f"\n{df_mutual_fund.head(5)}\n\n\n")
    #print("Mutual Funds Dataframe:", f"\n{df_mutual_fund.head(10)}")


def test_haunted_df():
    """Test out the Pandas bug where if columns aren't all pushed over, it cannot read data correctly"""
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


# CLEAN
def clean_percentage_columns(df, columns):
    """
    Clean percentage columns in a dataframe.
    
    Args:
        df (pd.DataFrame): Input dataframe
        columns (list): List of column names to clean
        
    Returns:
        pd.DataFrame: Dataframe with cleaned percentage columns
    """
    def convert_percentage(x):
        """Clean values in dataframe."""
        # Check if value is missing/null
        if pd.isna(x):
            return None
        # Check if object is an int or float already
        if isinstance(x, (int, float)):
            return x
        # If value is a string, check for invalid. If a percentage, remove '%' and any whitespace, convert to float.
        if isinstance(x, str):
            x = x.strip()
            if x in ['--', '', 'N/A', 'nan']:
                return None
            try:
                # Remove '%' and any whitespace, then convert to float
                return float(x.replace('%', '').strip())
            except ValueError:
                return None
        return None

    df_cleaned = df.copy()
    
    # Validate data was cleaned. If not, log an issue.
    for col in columns:
        if col in df.columns:
            df_cleaned[col] = df_cleaned[col].apply(convert_percentage)
        else:
            print(f"Warning: Column '{col}' not found in dataframe")
            
    return df_cleaned


def check_remaining_strings(df, columns):
    """Check for any remaining string values in specified columns."""
    for col in columns:
        string_values = df[df[col].apply(lambda x: isinstance(x, str))]
        if not string_values.empty:
            print(f"\nWarning: Found string values in {col}:")
            print(string_values[col].unique())


def validate_percentage_conversion(df, columns):
    """Data insights and Validate percentage conversion results."""
    validation_results = {}
    
    for col in columns:
        if col not in df.columns:
            validation_results[col] = "Column not found"
            continue
            
        column_data = df[col]
        validation_results[col] = {
            "null_count": column_data.isnull().sum(),
            "non_numeric": sum(
                ~column_data.isnull() & 
                column_data.apply(lambda x: not isinstance(x, (int, float)))
            ),
            "min_value": column_data.min(),
            "max_value": column_data.max(),
            "mean_value": column_data.mean()
        }
    
    return validation_results


# FILTER
def get_range_values(level, metric, ETF_LEVELS):
    """
    Get min and max values for a given level and metric
    """
    levels = list(ETF_LEVELS[metric].keys())
    values = list(ETF_LEVELS[metric].values())
    
    current_idx = levels.index(level)
    
    # If it's the first level (e.g., "Low")
    if current_idx == 0:
        min_val = 0
        max_val = values[current_idx]
    # If it's the last level
    elif current_idx == len(levels) - 1:
        min_val = values[current_idx - 1]
        max_val = values[current_idx]
    # For levels in between
    else:
        min_val = values[current_idx - 1]
        max_val = values[current_idx]
        
    return min_val, max_val


from constants import ETF_LEVELS
def filter_etfs_with_ranges(df, risk_level='Low', expense_level='Low', return_level='Low'):
    """
    Filter ETFs with range information and summary
    """
    # Get range values
    risk_min, risk_max = get_range_values(risk_level, 'Risk', ETF_LEVELS)
    expense_min, expense_max = get_range_values(expense_level, 'Expense Ratio', ETF_LEVELS)
    return_min, return_max = get_range_values(return_level, 'Return', ETF_LEVELS)
    
    # Create filters
    risk_filter = (df['3-Year Alpha'] > risk_min) & (df['3-Year Alpha'] <= risk_max)
    expense_filter = (df['Expense Ratio'] > expense_min) & (df['Expense Ratio'] <= expense_max)
    return_filter = (df['1 Yr Return'] > return_min) & (df['1 Yr Return'] <= return_max)
    
    # Apply filters
    filtered_df = df[risk_filter & expense_filter & return_filter]
    
    # Create summary
    summary = {
        'Risk Level': risk_level,
        'Expense Level': expense_level,
        'Return Level': return_level,
        f'{risk_level} Risk Range': f"{risk_min:.2f} - {risk_max:.2f}",
        f'{expense_level} Expense Ratio Range': f"{expense_min:.2f} - {expense_max:.2f}",
        f'{return_level} Return Range': f"{return_min:.2f} - {return_max:.2f}",
        'Total ETFs Found': len(filtered_df),
    }
    
    # Sort by 1 Year Return in descending order
    return filtered_df.sort_values('1 Yr Return', ascending=False), summary
