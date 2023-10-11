def load_data(file_path):
    """
    Load the credit card clients data from a specified file.

    Parameters:
    file_path (str): The path to the data file.

    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    df = pd.read_csv(file_path, header=1, sep='\t')
    df.rename({'default payment next month': 'DEFAULT'}, axis='columns', inplace=True)
    return df