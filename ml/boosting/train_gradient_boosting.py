from pathlib import Path

import joblib
from sklearn.ensemble import GradientBoostingRegressor

from ml.evaluate_model import calculate_metrics, save_metrics
from ml.preprocessing import preprocess_data


BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "gradient_boosting.pkl"


def main():
    """Train and evaluate a Gradient Boosting Regressor."""

    X_train, X_test, y_train, y_test, _ = preprocess_data()

    model = GradientBoostingRegressor(
        random_state=42,
    )

    model.fit(
        X_train,
        y_train,
    )

    model_name = "gradient_boosting"

    metrics = calculate_metrics(
        model,
        X_test,
        y_test,
        model_name,
    )


    # ensure the models directory exists
    MODEL_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    
    # Save trained model
    joblib.dump(
        model,
        MODEL_PATH,
    )

    # Save evaluation metrics
    save_metrics(
        metrics,
        model_name,
    )

    print("\n========== Gradient Boosting Training Complete ==========")
    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    main()

"""run using 
py -m ml.boosting.train_gradient_boosting
this treats the "ml" dir as a package and allows the import statements to work correctly.
"""