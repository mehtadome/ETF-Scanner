import pandas as pd
from ...calcs.constants import COLUMNS_TO_CLEAN, COLUMNS_TO_KEEP

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


# Usage
from ...utils.exports import init_table
def test_cleaning():
    df_etf = init_table.export_combined_sheets_loggerless()
    try:
        # Print the columns in this df
        print(f"Columns in the dataframe:\n {df_etf.columns.str.strip()}")
        # Clean the percentage columns
        df_etf = clean_percentage_columns(df_etf, COLUMNS_TO_CLEAN)
        
        # Verify the conversion
        print("\nSample of cleaned data:")
        print(df_etf[COLUMNS_TO_CLEAN].head())
        
        # Check for any remaining string values
        check_remaining_strings(df_etf, COLUMNS_TO_CLEAN)
                
    except Exception as e:
        print(f"Error cleaning percentage columns: {str(e)}")

    try:
        # Usage with validation
        # df_etf = clean_percentage_columns(df_etf, COLUMNS_TO_CLEAN)
        validation_results = validate_percentage_conversion(df_etf, COLUMNS_TO_CLEAN)

        for col, results in validation_results.items():
                print(f"\nValidation results for {col}:")
                if isinstance(results, dict):  # Check if results is a dictionary
                    for metric, value in results.items():
                        print(f"{metric}: {value}")
                else:
                    print(results)  # Print the error message directly

    except Exception as e:
        print(f"Error during validation: {str(e)}")
# test_cleaning()