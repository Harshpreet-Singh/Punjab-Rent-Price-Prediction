from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

from preprocessing import preprocess_data
from evaluate_model import calculate_metrics, save_metrics

BASE_DIR = Path(__file__).resolve().parent.parent

MODELS_DIR = BASE_DIR / "models"
METRICS_DIR = BASE_DIR / "outputs" / "metrics"

def load_preprocessed_data():
    """ Load and preprocess the dataset. """

    X_train, X_test, y_train, y_test, _ = preprocess_data()

    return X_train, X_test, y_train, y_test


def create_param_grid():
    """ Define the hyperparameter search space. """

    param_grid = {
        "n_estimators": [100, 200],
        "max_depth": [10, 20, None],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2],
    }

    return param_grid


def tune_model(X_train, y_train, param_grid):
    """ Tune the Random Forest model using GridSearchCV. """

    model = RandomForestRegressor(random_state=42)

    grid_search = GridSearchCV(
        estimator=model,            # tells GridSearchCV which model to tune.   
        param_grid=param_grid,      # dictionary we created earlier.
        cv=5,                       # 5-Fold Cross Validation. Every hyperparameter combination is evaluated 5 times.
        scoring="r2",               # Since our project compares models using R², we'll continue using it
        n_jobs=-1,                  # Use all CPU cores. Much faster.
        verbose=2,                  # for formatting the output
        refit=True,                 # After finding the best hyperparameters, GridSearchCV automatically trains one final model on the entire training set.
    )

    print("\nStarting Grid Search...\n")

    grid_search.fit(X_train, y_train)

    return grid_search


def save_model(model):
    """ Save the tuned Random Forest model. """

    model_path = MODELS_DIR / "random_forest_tuned.pkl"

    joblib.dump(model, model_path)

    print(f"\nModel saved to: {model_path}")

def main():
    print("Loading preprocessed data...")

    X_train, X_test, y_train, y_test = load_preprocessed_data()

    print(f"Training samples : {X_train.shape[0]}")          # len() don't work here so use shape[0] here 0 gives - Number of rows, and [1] gives no. of columns
    print(f"Testing samples  : {X_test.shape[0]}")

    print("\nCreating parameter grid...")

    param_grid = create_param_grid()

    grid_search = tune_model(
        X_train,
        y_train,
        param_grid,
    )

    print("\nGrid Search Completed!")

    print("\nBest Parameters:")
    print(grid_search.best_params_)

    print(f"\nBest Cross Validation R²: {grid_search.best_score_:.4f}")

    # model saving script below: 

    best_model = grid_search.best_estimator_

    metrics = calculate_metrics(
        best_model,
        X_test,
        y_test,
        "random_forest_tuned",
    )

    save_metrics(
        metrics,
        "random_forest_tuned",
    )

    save_model(best_model)

    print("\nTest Set Performance:")

    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")

if __name__ == "__main__":
    main()