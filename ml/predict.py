"""
predict.py

Predict house rent using a trained machine learning model.
"""

from pathlib import Path

import joblib
import pandas as pd


# ============================================================
# Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_NAME = "random_forest_tuned"

MODELS_DIR = BASE_DIR / "models"

MODEL_PATH = MODELS_DIR / f"{MODEL_NAME}.pkl"
PREPROCESSOR_PATH = MODELS_DIR / "preprocessor.pkl"


# ============================================================
# Model Loading
# ============================================================

def load_model():
    """Load the trained model."""

    return joblib.load(MODEL_PATH)


def load_preprocessor():
    """Load the fitted preprocessor."""

    return joblib.load(PREPROCESSOR_PATH)


# ============================================================
# User Input Helpers
# ============================================================

def get_positive_integer(prompt):
    """Get a positive integer from the user."""

    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("Please enter a value greater than 0.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_non_empty_input(prompt):
    """Get a non-empty string from the user."""

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


# ============================================================
# Feature Engineering
# ============================================================

def create_area_category(area):
    """Create area category using the same training thresholds."""

    if area <= 750:
        return "Small"
    elif area <= 1680:
        return "Medium"
    else:
        return "Large"


# ============================================================
# User Input
# ============================================================

def get_choice(prompt, options):
    """Display numbered options and return the selected value."""

    print(f"\n{prompt}")

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    while True:
        try:
            choice = int(input("Enter choice: "))

            if 1 <= choice <= len(options):
                return options[choice - 1]

            print(f"Please enter a number between 1 and {len(options)}.")

        except ValueError:
            print("Please enter a valid number.")


def get_user_input():
    """Get property details from the user."""

    print("\n========== Enter Property Details ==========\n")

    bhk = get_positive_integer("BHK: ")

    bathroom = get_positive_integer("Bathroom: ")

    area = get_positive_integer("Area (sqft): ")

    location = get_non_empty_input("Location: ")

    city = get_non_empty_input("City: ")

    furnishing = get_choice(
        "Furnishing:",
        [
            "Fully Furnished",
            "Semi Furnished",
            "Furnished",
            "Unknown",
        ],
    )

    property_type = get_choice(
        "Property Type:",
        [
            "Apartment",
            "Flat",
            "Independent House",
            "Independent Floor",
            "Room Set",
            "PG",
            "Unknown",
        ],
    )

    area_category = create_area_category(area)

    input_data = pd.DataFrame({
        "bhk": [bhk],
        "bathroom": [bathroom],
        "area": [area],
        "location": [location],
        "city": [city],
        "area_category": [area_category],
        "furnishing": [furnishing],
        "property_type": [property_type],
    })

    return input_data



# ============================================================
# Prediction
# ============================================================

def predict_rent(model, preprocessor, input_data):
    """Predict rent using the trained model."""

    transformed_data = preprocessor.transform(input_data)

    prediction = model.predict(transformed_data)

    return prediction[0]


# ============================================================
# Main
# ============================================================

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
    print(f"Estimated Monthly Rent: ₹{predicted_rent:,.2f}")


if __name__ == "__main__":
    main()
