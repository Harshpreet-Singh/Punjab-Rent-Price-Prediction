from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestRegressor

from preprocessing import preprocess_data


MODEL_DIR = Path("./models")
MODEL_PATH = MODEL_DIR / "random_forest.pkl"


def train_random_forest():
    """ Train a Random Forest Regressor and save the trained model. """

    print("Loading preprocessed data...")

    X_train, X_test, y_train, y_test, preprocessor = preprocess_data()

    print("Training Random Forest model...")

    model = RandomForestRegressor(
        n_estimators=100,    # n_estimators = Number of Trees
        random_state=42      # to maintain randomness
    )

    model.fit(X_train, y_train)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    print("Training completed successfully.")
    print(f"Model saved to: {MODEL_PATH}")


def main():
    train_random_forest()


if __name__ == "__main__":
    main()