"""
preprocessing.py

Purpose:
Prepare the rental dataset for Machine Learning.

Steps to be implemented:
1. Load dataset
2. Inspect data
3. Select features and target
4. Encode categorical features
5. Split train and test data
"""
import pandas as pd

# Dataset path
DATA_PATH = "../data/punjab_rental_dataset.csv"


def load_dataset():
    """
    Load the cleaned rental dataset.
    """

    df = pd.read_csv(DATA_PATH)
    return df


def main():

    df = load_dataset()

    print(df.head())


if __name__ == "__main__":
    main()