from ...calcs.constants import ETF_LEVELS

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


def filter_etfs_with_ranges(df, risk_level='Low', expense_level='Low', return_level='Low'):
    """
    Filter ETFs with range information and summary
    """
    # Get range values
    risk_min, risk_max = get_range_values(risk_level, 'Risk', ETF_LEVELS)
    expense_min, expense_max = get_range_values(expense_level, 'Expense Ratio', ETF_LEVELS)
    return_min, return_max = get_range_values(return_level, 'Return', ETF_LEVELS)
    
    # Create filters
    risk_filter = (df['Risk'] > risk_min) & (df['Risk'] <= risk_max)
    expense_filter = (df['Expense Ratio'] > expense_min) & (df['Expense Ratio'] <= expense_max)
    return_filter = (df['Return'] > return_min) & (df['Return'] <= return_max)
    
    # Apply filters
    filtered_df = df[risk_filter & expense_filter & return_filter]
    
    # Create summary
    summary = {
        'Risk Range': f"{risk_min:.2f} - {risk_max:.2f}",
        'Expense Ratio Range': f"{expense_min:.2f} - {expense_max:.2f}",
        'Return Range': f"{return_min:.2f} - {return_max:.2f}",
        'Total ETFs Found': len(filtered_df),
        'Risk Level': risk_level,
        'Expense Level': expense_level,
        'Return Level': return_level
    }
    
    return filtered_df.sort_values('Expense Ratio'), summary

# Usage with summary
try:
    filtered_etfs, summary = filter_etfs_with_ranges(
        df_etf,
        risk_level='Medium',
        expense_level='Low',
        return_level='High'
    )
    
    # Print summary
    print("\nFilter Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")
    
    # Print filtered ETFs
    print("\nFiltered ETFs:")
    print(filtered_etfs)
    
except Exception as e:
    print(f"Error filtering ETFs: {str(e)}")