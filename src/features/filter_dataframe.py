def filter_dataframe(df, columns_to_filter):
    """
    Filter a DataFrame based on specified columns.

    This function filters the input DataFrame to exclude rows where all the specified columns
    have values equal to 0.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame to be filtered.
    - columns_to_filter (list): A list of column names to be used for filtering.

    Returns:
    - pandas.DataFrame: The filtered DataFrame.
    """
    # Create a condition that checks if all specified columns are not equal to 0
    condition = df[columns_to_filter].ne(0).all(axis=1)
    
    # Use the condition to filter the DataFrame
    filtered_df = df.loc[condition]
    
    return filtered_df