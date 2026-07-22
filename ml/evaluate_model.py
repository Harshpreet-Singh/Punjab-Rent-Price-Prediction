"""
evaluate_model.py

Evaluate the trained Linear Regression model.
"""

import joblib
from math import sqrt

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from preprocessing import preprocess_data


# MODEL_PATH = "./models/linear_regression.pkl"
# METRICS_PATH = "./outputs/metrics/linear_regression_metrics.txt"

MODEL_NAME = "decision_tree"

MODEL_PATH = f"./models/{MODEL_NAME}.pkl"
METRICS_PATH = f"./outputs/metrics/{MODEL_NAME}_metrics.txt"

def load_model():
    """
    Load the trained model.
    """

    model = joblib.load(MODEL_PATH)

    return model


def evaluate():

    print("Loading trained model...")

    model = load_model()

    print("Loading preprocessed data...")

    X_train, X_test, y_train, y_test, _ = preprocess_data()

    print("Making predictions...")

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    mse = mean_squared_error(y_test, predictions)

    rmse = sqrt(mse)

    r2 = r2_score(y_test, predictions)

    print("\n========== Evaluation ==========")

    print(f"MAE  : {mae:.2f}")

    print(f"MSE  : {mse:.2f}")

    print(f"RMSE : {rmse:.2f}")

    print(f"R²   : {r2:.4f}")

    with open(METRICS_PATH, "w") as file:

        file.write("Linear Regression Evaluation\n")
        file.write("=" * 35 + "\n\n")

        file.write(f"MAE  : {mae:.2f}\n")
        file.write(f"MSE  : {mse:.2f}\n")
        file.write(f"RMSE : {rmse:.2f}\n")
        file.write(f"R²   : {r2:.4f}\n")

    print(f"\nMetrics saved to: {METRICS_PATH}")


def main():

    evaluate()


if __name__ == "__main__":
    main()