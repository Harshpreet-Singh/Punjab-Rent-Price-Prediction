"""
train_lightgbm.py

Purpose:
Train and evaluate a LightGBM Regressor.
"""

from pathlib import Path

import joblib
from lightgbm import LGBMRegressor

from ml.evaluate_model import calculate_metrics, save_metrics
from ml.preprocessing import preprocess_data

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "lightgbm.pkl"

METRICS_PATH = (
    BASE_DIR
    / "outputs"
    / "metrics"
    / "lightgbm_metrics.txt"
)


def main():
    """Train and evaluate a LightGBM Regressor."""

    print("Loading and preprocessing data...")

    X_train, X_test, y_train, y_test, preprocessor = preprocess_data()

    print("Training LightGBM model...")

    model = LGBMRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=-1,
        num_leaves=31,
        random_state=42,
    )

    model.fit(X_train, y_train)

    print("Evaluating model...")

    metrics = calculate_metrics(
        model,
        X_test,
        y_test,
        "lightgbm",
    )

    print("Saving model...")

    joblib.dump(model, MODEL_PATH)

    print("Saving metrics...")

    save_metrics(metrics, "lightgbm")

    print("\n=== LightGBM Results ===")
    print(f"Model: {metrics['Model']}")
    print(f"MAE  : {metrics['MAE']:.2f}")
    print(f"MSE  : {metrics['MSE']:.2f}")
    print(f"RMSE : {metrics['RMSE']:.2f}")
    print(f"R²   : {metrics['R2']:.4f}")

    print(f"\nModel saved to: {MODEL_PATH}")
    print(f"Metrics saved to: {METRICS_PATH}")


if __name__ == "__main__":
    main()