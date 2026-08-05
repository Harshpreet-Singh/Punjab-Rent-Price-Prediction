from pathlib import Path

import joblib
from xgboost import XGBRegressor

from ml.evaluate_model import calculate_metrics, save_metrics
from ml.preprocessing import preprocess_data

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "xgboost.pkl"
def main():
    """Train and evaluate an XGBoost Regressor."""

    X_train, X_test, y_train, y_test, _ = preprocess_data()
    model = XGBRegressor(
        random_state=42,
        verbosity=0,
        eval_metric="rmse",                # It aligns the model's training feedback with the metrics you're comparing across models.
    )

    model.fit(
        X_train,
        y_train,
    )

    model_name = "xgboost"

    # evaluate the model
    metrics = calculate_metrics(
        model,
        X_test,
        y_test,
        model_name,
    )

    # save the model
    joblib.dump(
        model,
        MODEL_PATH,
    )

    # save the metrics
    save_metrics(
        metrics,
        model_name,
    )
    print("\n========== XGBoost Training Complete ==========")
    print(f"Model saved to: {MODEL_PATH}")  

if __name__ == "__main__":
    main()