"""
evaluate_model.py

│
├── load_model()
│
├── calculate_metrics()
│
├── save_metrics()
│
├── evaluate()
│
└── main()

Evaluate any trained machine learning model.
"""

from math import sqrt
from pathlib import Path

import joblib

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from ml.preprocessing import preprocess_data

BASE_DIR = Path(__file__).resolve().parent.parent

MODELS_DIR = BASE_DIR / "models"
METRICS_DIR = BASE_DIR / "outputs" / "metrics"


def load_model(model_name):
    """ Load a trained model. """

    model_path = MODELS_DIR / f"{model_name}.pkl"

    return joblib.load(model_path)


def calculate_metrics(model, X_test, y_test, model_name):
    """
    Calculate evaluation metrics.
    """

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    mse = mean_squared_error(y_test, predictions)

    rmse = sqrt(mse)

    r2 = r2_score(y_test, predictions)

    return {
        "Model": model_name_to_title(model_name),
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2": r2,
    }


def save_metrics(metrics, model_name, verbose=True):
    """ Save metrics to a text file. """

    METRICS_DIR.mkdir(parents=True, exist_ok=True)

    metrics_path = METRICS_DIR / f"{model_name}_metrics.txt"

    with open(metrics_path, "w") as file:

        file.write(f"{model_name_to_title(model_name)} Evaluation\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"MAE  : {metrics['MAE']:.2f}\n")
        file.write(f"MSE  : {metrics['MSE']:.2f}\n")
        file.write(f"RMSE : {metrics['RMSE']:.2f}\n")
        file.write(f"R²   : {metrics['R2']:.4f}\n")

    if verbose:
        print(f"\nMetrics saved to: {metrics_path}")


def model_name_to_title(model_name):
    """ Convert file name into readable title. """

    return model_name.replace("_", " ").title()


def evaluate(model_name, verbose=True):
    """ Evaluate a trained model. """

    if verbose:
        print("Loading trained model...")

    model = load_model(model_name)

    if verbose:
        print("Loading preprocessed data...")

    _, X_test, _, y_test, _ = preprocess_data()

    if verbose:
        print("Making predictions...")

    metrics = calculate_metrics(model, X_test, y_test, model_name)

    if verbose:
        print("\n========== Evaluation ==========")

        print(f"Model: {metrics['Model']}")
        print(f"MAE  : {metrics['MAE']:.2f}")
        print(f"MSE  : {metrics['MSE']:.2f}")
        print(f"RMSE : {metrics['RMSE']:.2f}")
        print(f"R²   : {metrics['R2']:.4f}")

    save_metrics(metrics, model_name, verbose)

    return metrics


def main():

    MODEL_NAME = "random_forest_tuned"

    evaluate(MODEL_NAME)


if __name__ == "__main__":
    main()



# ------------------------------------------------------------------
# Verbose ka simple matlab:
#
# "verbose" decide karta hai ki program run hote time terminal me
# messages print honge ya nahi.
#
# Agar verbose=True hai:
# - "Loading trained model..." print hoga.
# - "Loading preprocessed data..." print hoga.
# - "Making predictions..." print hoga.
# - Saare evaluation metrics (MAE, MSE, RMSE, R²) screen par dikhengi.
# - Metrics kis file me save hui hain, uska path bhi print hoga.
#
# Agar verbose=False hai:
# - Program bilkul same kaam karega.
# - Model evaluate hoga.
# - Metrics calculate hongi.
# - Metrics file bhi save hogi.
# - Bas terminal me koi messages print nahi honge.
#
# Matlab verbose sirf output (print statements) ko control karta hai.
# Iska evaluation, prediction ya metrics ke results par koi effect nahi padta.
#
# Example:
# evaluate("random_forest_tuned", verbose=True)   # Sab messages dikhenge.
# evaluate("random_forest_tuned", verbose=False)  # Silent mode me chalega.
# ------------------------------------------------------------------