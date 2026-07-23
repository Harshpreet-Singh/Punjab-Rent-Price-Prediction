from pathlib import Path

import joblib
from sklearn.tree import DecisionTreeRegressor

from preprocessing import preprocess_data


MODEL_DIR = Path("./models")
MODEL_PATH = MODEL_DIR / "decision_tree.pkl"


def train_decision_tree():
    """ Train a Decision Tree Regressor and save the trained model. """

    print("Loading preprocessed data...")

    X_train, X_test, y_train, y_test, preprocessor = preprocess_data()

    print("Training Decision Tree model...")

#   Model Creation - Create a Decision Tree. Don't let it grow beyond 5 levels, and keep the results reproducible
    MAX_DEPTH = 5
    RANDOM_STATE = 42

    model = DecisionTreeRegressor(
        max_depth=MAX_DEPTH,
        random_state=RANDOM_STATE
    )

#   Training
    model.fit(X_train, y_train)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)

#   Saving
    joblib.dump(model, MODEL_PATH)

    print(f"Training completed successfully.")
    print(f"Model saved to: {MODEL_PATH}")


def main():
    train_decision_tree()


if __name__ == "__main__":
    main()