"""
predict.py

Predict house rent using a trained machine learning model.
"""

from pathlib import Path

import joblib
import pandas as pd


MODEL_NAME = "random_forest"

MODELS_DIR = Path("./models")

MODEL_PATH = MODELS_DIR / f"{MODEL_NAME}.pkl"
PREPROCESSOR_PATH = MODELS_DIR / "preprocessor.pkl"


def load_model():
    """
    Load the trained model.
    """

    return joblib.load(MODEL_PATH)


def load_preprocessor():
    """
    Load the fitted preprocessor.
    """

    return joblib.load(PREPROCESSOR_PATH)


def get_user_input():
    """
    Get property details from the user.
    """

    print("\n========== Enter Property Details ==========\n")

    bhk = int(input("BHK: "))
    bathroom = int(input("Bathroom: "))
    area = int(input("Area (sqft): "))
    location = input("Location: ").strip()
    city = input("City: ").strip()

    input_data = pd.DataFrame({
        "bhk": [bhk],
        "bathroom": [bathroom],
        "area": [area],
        "location": [location],
        "city": [city],
    })

    return input_data


def predict_rent(model, preprocessor, input_data):
    """
    Predict rent using the trained model.
    """

    transformed_data = preprocessor.transform(input_data)

    prediction = model.predict(transformed_data)

    return prediction[0]


def main():

    print("=" * 50)
    print("Punjab Rent Price Prediction")
    print("=" * 50)

    model = load_model()

    preprocessor = load_preprocessor()

    input_data = get_user_input()

    predicted_rent = predict_rent(
        model,
        preprocessor,
        input_data,
    )

    print("\n========== Prediction ==========")
    print(f"Predicted Rent: ₹{predicted_rent:,.2f}")


if __name__ == "__main__":
    main()