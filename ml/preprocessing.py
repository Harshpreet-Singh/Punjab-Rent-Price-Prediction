"""
preprocessing.py

Purpose:
Prepare the rental dataset for Machine Learning.
"""

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Dataset path
DATA_PATH = "data/punjab_rental_dataset.csv"


def load_dataset():
    """Load the cleaned rental dataset."""
    return pd.read_csv(DATA_PATH)


def inspect_dataset(df):
    """Display basic information about the dataset."""

    print("\n========== Dataset Shape ==========")
    print(df.shape)

    print("\n========== Columns ==========")
    print(df.columns.tolist())

    print("\n========== Data Types ==========")
    print(df.dtypes)

    print("\n========== Missing Values ==========")
    print(df.isnull().sum())

    print("\n========== First 5 Rows ==========")
    print(df.head())

    print("\n========== Statistical Summary ==========")
    print(df.describe())


def select_features_target(df):
    """Separate features and target."""

    X = df[
        [
            "bhk",
            "bathroom",
            "area",
            "location",
            "city",
        ]
    ]

    y = df["price"]

    return X, y


def split_data(X, y):
    """Split dataset into train and test sets."""

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )


def encode_features(X_train, X_test):
    """
    Encode categorical columns using One-Hot Encoding.
    """

    categorical_features = [
        "location",
        "city",
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features,
            )
        ],
        remainder="passthrough",
    )

    X_train_encoded = preprocessor.fit_transform(X_train)

    X_test_encoded = preprocessor.transform(X_test)

    return X_train_encoded, X_test_encoded, preprocessor


def main():

    # Load dataset
    df = load_dataset()

    # Inspect dataset
    inspect_dataset(df)

    # Feature selection
    X, y = select_features_target(df)

    # Train-test split
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Encode features
    X_train_encoded, X_test_encoded, preprocessor = encode_features(
        X_train,
        X_test,
    )

    print("\n========== Encoded Data ==========")
    print(f"X_train Shape : {X_train_encoded.shape}")
    print(f"X_test Shape  : {X_test_encoded.shape}")


if __name__ == "__main__":
    main()