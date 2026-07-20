"""
train_model.py

Train a Linear Regression model
using the preprocessed rental dataset.
"""

import joblib
from sklearn.linear_model import LinearRegression       # importing the algorithm.
from preprocessing import preprocess_data


MODEL_PATH = "./models/linear_regression.pkl"


def train_model():

    print("Loading preprocessed data...")

    X_train, X_test, y_train, y_test, preprocessor = preprocess_data()

    print("Training Linear Regression model...")

    model = LinearRegression()                 # Just an empty model is made here

    model.fit(X_train, y_train)                # This is where learning happens.

    print("Training completed successfully.")

    return model, preprocessor, X_test, y_test


def save_model(model):

    joblib.dump(model, MODEL_PATH)

    print(f"Model saved to: {MODEL_PATH}")

# why joblib : 
# Because ML models are Python objects.

# They cannot be saved as plain text.

# Joblib specializes in saving trained models efficiently.

def main():

    model, preprocessor, X_test, y_test = train_model()

    save_model(model)


if __name__ == "__main__":
    main()