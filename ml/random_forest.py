from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestRegressor

from preprocessing import preprocess_data


MODEL_DIR = Path("./models")

MODEL_PATH = MODEL_DIR / "random_forest.pkl"
PREPROCESSOR_PATH = MODEL_DIR / "preprocessor.pkl"


def train_random_forest():
    """Train a Random Forest Regressor and save the trained model."""

    print("Loading preprocessed data...")

    X_train, X_test, y_train, y_test, preprocessor = preprocess_data()

    print("Training Random Forest model...")

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
    )

    model.fit(X_train, y_train)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    # Save trained model
    joblib.dump(model, MODEL_PATH)

    # Save fitted preprocessor
    joblib.dump(preprocessor, PREPROCESSOR_PATH)

    print("Training completed successfully.")
    print(f"Model saved to: {MODEL_PATH}")
    print(f"Preprocessor saved to: {PREPROCESSOR_PATH}")


def main():
    train_random_forest()


if __name__ == "__main__":
    main()