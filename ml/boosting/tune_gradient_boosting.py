# py -m ml.boosting.tune_gradient_boosting
from pathlib import Path

import joblib
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

from ml.evaluate_model import calculate_metrics, save_metrics
from ml.preprocessing import preprocess_data

BASE_DIR = Path(__file__).resolve().parents[2]

MODELS_DIR = BASE_DIR / "models"
METRICS_DIR = BASE_DIR / "outputs" / "metrics"

def load_preprocessed_data():
    """Load and preprocess the dataset."""

    return preprocess_data()

def create_param_grid():
    """Define the hyperparameter search space."""

    param_grid = {
        "n_estimators": [100, 200],
        "learning_rate": [0.05, 0.1],
        "max_depth": [3, 5],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2],
    }

    return param_grid

def tune_model(X_train, y_train, param_grid):
    """Tune the Gradient Boosting model using GridSearchCV."""

    model = GradientBoostingRegressor( 
        random_state=42,
    )

    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=5,
        scoring="r2",
        n_jobs=-1,
        verbose=2,
        refit=True,
    )

    print("\nStarting Grid Search...\n")

    grid_search.fit(
        X_train,
        y_train,
    )

    return grid_search


def save_model(model):
    """Save the tuned Gradient Boosting model."""

    MODELS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    model_path = MODELS_DIR / "gradient_boosting_tuned.pkl"

    joblib.dump(
        model,
        model_path,
    )

    print(f"\nModel saved to: {model_path}")


def save_preprocessor(preprocessor):
    """Save the fitted preprocessing pipeline."""

    MODELS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    preprocessor_path = MODELS_DIR / "preprocessor.pkl"

    joblib.dump(
        preprocessor,
        preprocessor_path,
    )

    print(f"\nPreprocessor saved to: {preprocessor_path}")

def main():

    print("Loading preprocessed data...")

    X_train, X_test, y_train, y_test, preprocessor = (
        load_preprocessed_data()
    )

    print(f"Training samples : {X_train.shape[0]}")
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

    print(
        f"\nBest Cross Validation R²: "
        f"{grid_search.best_score_:.4f}"
    )

    best_model = grid_search.best_estimator_

    metrics = calculate_metrics(
        best_model,
        X_test,
        y_test,
        "gradient_boosting_tuned",
    )

    save_metrics(
        metrics,
        "gradient_boosting_tuned",
    )

    save_model(best_model)
    save_preprocessor(preprocessor)

    print("\n========== Tuned Model Performance ==========")

    print(f"Model : {metrics['Model']}")
    print(f"MAE   : {metrics['MAE']:.2f}")
    print(f"MSE   : {metrics['MSE']:.2f}")
    print(f"RMSE  : {metrics['RMSE']:.2f}")
    print(f"R²    : {metrics['R2']:.4f}")


if __name__ == "__main__":
    main()