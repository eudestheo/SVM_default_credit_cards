def split_and_scale_data(X, y, random_state=42):
    """
    Split and scale the data into training and testing sets.

    Parameters:
    - X: Features DataFrame.
    - y: Target variable Series.
    - random_state (int): Random seed for reproducibility (default is 42).

    Returns:
    - DataFrame: X_train_scaled - Scaled training features.
    - DataFrame: X_test_scaled - Scaled testing features.
    - Series: y_train - Training target variable.
    - Series: y_test - Testing target variable.
    """
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=random_state)

    # Fit a StandardScaler on the training data and transform both training and testing data
    scaler = preprocessing.StandardScaler().fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test