"""
preprocessing.py

Purpose:
Prepare the rental dataset for Machine Learning.

Pipeline:
1. Load dataset
2. Inspect dataset
3. Select features and target
4. Split train and test data
"""

import pandas as pd
from sklearn.model_selection import train_test_split

# Dataset path
DATA_PATH = "data/punjab_rental_dataset.csv"


def load_dataset():
    """
    Load the cleaned rental dataset.
    """
    df = pd.read_csv(DATA_PATH)
    return df


def inspect_dataset(df):
    """
    Display basic information about the dataset.
    """

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
    """
    Separate features (X) and target (y).
    """

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
    """
    Split the dataset into training and testing sets.
    """

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    return X_train, X_test, y_train, y_test


def main():
    """
    Execute the preprocessing pipeline.
    """

    # Load dataset
    df = load_dataset()

    # Inspect dataset
    inspect_dataset(df)

    # Select features and target
    X, y = select_features_target(df)

    # Split dataset
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Display split information
    print("\n========== Train-Test Split ==========")
    print(f"X_train Shape : {X_train.shape}")
    print(f"X_test Shape  : {X_test.shape}")
    print(f"y_train Shape : {y_train.shape}")
    print(f"y_test Shape  : {y_test.shape}")


if __name__ == "__main__":
    main()