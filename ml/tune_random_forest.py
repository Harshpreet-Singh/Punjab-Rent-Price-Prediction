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


def tune_model():
    pass


def save_model():
    pass


def main():
    print("Loading preprocessed data...")

    X_train, X_test, y_train, y_test = load_preprocessed_data()

    print(f"Training samples : {len(X_train)}")
    print(f"Testing samples  : {len(X_test)}")

    print("\nCreating parameter grid...")

    param_grid = create_param_grid()

    print("Parameter Grid:")

    for parameter, values in param_grid.items():
        print(f"{parameter}: {values}")


if __name__ == "__main__":
    main()