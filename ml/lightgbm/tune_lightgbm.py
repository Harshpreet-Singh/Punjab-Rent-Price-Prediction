"""
tune_lightgbm.py

Purpose:
Tune a LightGBM Regressor using GridSearchCV.
"""

from pathlib import Path

import joblib
from lightgbm import LGBMRegressor
from sklearn.model_selection import GridSearchCV

from ml.evaluate_model import calculate_metrics, save_metrics
from ml.preprocessing import preprocess_data

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "lightgbm_tuned.pkl"


def main():
    """Tune a LightGBM Regressor."""

    print("Loading and preprocessing data...")

    X_train, X_test, y_train, y_test, _ = preprocess_data()

    print("Creating LightGBM model...")

    model = LGBMRegressor(random_state=42)

    param_grid = {
        "n_estimators": [100, 200, 300],
        "learning_rate": [0.01, 0.05, 0.1],
        "num_leaves": [31, 50, 70],
        "max_depth": [-1, 10, 20],
        "min_child_samples": [20, 30],
    }

    print("Running GridSearchCV...")

    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        scoring="r2",
        cv=5,
        n_jobs=-1,
        verbose=2,
    )

    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    print("\nBest Parameters:")
    print(grid_search.best_params_)

    print(f"\nBest Cross Validation R²: {grid_search.best_score_:.4f}")

    print("\nEvaluating tuned model...")

    metrics = calculate_metrics(
        best_model,
        X_test,
        y_test,
        "lightgbm_tuned",
    )

    print("Saving tuned model...")

    joblib.dump(best_model, MODEL_PATH)

    print("Saving metrics...")

    save_metrics(metrics, "lightgbm_tuned")

    print("\n=== Tuned LightGBM Results ===")
    print(f"Model: {metrics['Model']}")
    print(f"MAE  : {metrics['MAE']:.2f}")
    print(f"MSE  : {metrics['MSE']:.2f}")
    print(f"RMSE : {metrics['RMSE']:.2f}")
    print(f"R²   : {metrics['R2']:.4f}")


if __name__ == "__main__":
    main()