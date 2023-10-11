def train_model(X, y):
    """
    Train the machine learning model using cross-validation and grid search.

    Parameters:
    X (DataFrame): Features (input variables) for training.
    y (Series): Target variable for training.

    Returns:
    XGBoostClassifier: The best-trained XGBoost model found by grid search.
    """
    # Define the machine learning model
    model = SVC(random_state=42)

    # Define hyperparameters for grid search
    param_grid =  {'C': [0.5, 1, 10, 100],
   'gamma': ['scale', 1, 0.1, 0.01, 0.001, 0.0001], 
   'kernel': ['rbf'],
    }

    # Perform grid search with cross-validation
    grid_search = GridSearchCV(estimator=model, 
                               param_grid=param_grid,
                                 scoring='accuracy',
                                 cv = 5,
                                 verbose=2)

    grid_search.fit(X, y)

    # Print the best hyperparameters
    print("Best Hyperparameters:", grid_search.best_params_)
    

    return grid_search.best_estimator_