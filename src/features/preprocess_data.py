def preprocess_data(df, target_column, categorical_columns=[]):
    """
    Prepare features and target variables.

    Parameters:
    - df: The DataFrame containing the data.
    - target_column (str): The name of the target variable column.
    - categorical_columns (list): List of column names to be one-hot encoded (if applicable).

    Returns:
    - DataFrame: Features DataFrame with one-hot encoding applied to
      specified categorical columns.
    - Series: Target variable Series.
    """
    # Create the target variable Series
    y = df[target_column].copy()

    # Create features DataFrame by dropping the target column
    X = df.drop(target_column, axis=1).copy()

    # Perform one-hot encoding on categorical columns
    X_encoded = pd.get_dummies(X, columns=categorical_columns)
    
    return X_encoded, y