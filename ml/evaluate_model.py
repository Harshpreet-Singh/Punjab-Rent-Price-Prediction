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

from preprocessing import preprocess_data


MODELS_DIR = Path("./models")
METRICS_DIR = Path("./outputs/metrics")


def load_model(model_name):
    """
    Load a trained model.
    """

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


def save_metrics(metrics, model_name):
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

    print(f"\nMetrics saved to: {metrics_path}")


def model_name_to_title(model_name):
    """ Convert file name into readable title. """

    return model_name.replace("_", " ").title()


def evaluate(model_name, verbose= True):
    """ Evaluate a trained model. """

    print("Loading trained model...")

    model = load_model(model_name)

    print("Loading preprocessed data...")

    _, X_test, _, y_test, _ = preprocess_data()

    print("Making predictions...")

    metrics = calculate_metrics(model, X_test, y_test, model_name)

    print("\n========== Evaluation ==========")

    print(f"Model: {metrics['Model']}")
    print(f"MAE  : {metrics['MAE']:.2f}")
    print(f"MSE  : {metrics['MSE']:.2f}")
    print(f"RMSE : {metrics['RMSE']:.2f}")
    print(f"R²   : {metrics['R2']:.4f}")

    save_metrics(metrics, model_name)

    return metrics


def main():

    MODEL_NAME = "random_forest"

    evaluate(MODEL_NAME)


if __name__ == "__main__":
    main()