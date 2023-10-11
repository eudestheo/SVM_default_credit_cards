def downsample_dataframe(df, column_to_downsample, n_samples=1000, random_state=42):
    """
    Downsample a DataFrame based on a specified column.

    This function performs downsampling on the input DataFrame by randomly selecting a
    specified number of samples from each category in the specified column.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame to be downsampled.
    - column_to_downsample (str): The name of the column to be used for downsampling.
    - n_samples (int): The number of samples to downsample to (default is 1000).
    - random_state (int): The random seed for reproducibility (default is 42).

    Returns:
    - pandas.DataFrame: The downsampled DataFrame.
    """
    # Split the DataFrame based on the specified column
    categories = df[column_to_downsample].unique()
    downsampled_dfs = []

    for category in categories:
        subset_df = df[df[column_to_downsample] == category]
        downsampled_subset = resample(subset_df, replace=False, n_samples=n_samples, random_state=random_state)
        downsampled_dfs.append(downsampled_subset)

    # Combine the downsampled DataFrames
    downsampled_df = pd.concat(downsampled_dfs)

    return downsampled_df