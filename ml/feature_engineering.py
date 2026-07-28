"""
Feature Engineering Module

This module is responsible for creating new features
from the existing dataset before model training.
"""


def add_area_category(df):
    """
    Create area category based on area distribution.

    Categories:
    Small   : <= 750 sqft
    Medium  : 750-1680 sqft
    Large   : > 1680 sqft
    """

    def categorize_area(area):
        if area <= 750:
            return "Small"
        elif area <= 1680:
            return "Medium"
        else:
            return "Large"

    df["area_category"] = df["area"].apply(categorize_area)

    return df


def extract_furnishing(df):
    """Extract furnishing information from title."""
    pass


def extract_property_type(df):
    """Extract property type from title."""
    pass


def create_engineered_features(df):
    """Apply all feature engineering steps."""
    pass

if __name__ == "__main__":
    from pathlib import Path
    import pandas as pd

    BASE_DIR = Path(__file__).resolve().parent.parent

    df = pd.read_csv(
        BASE_DIR / "data" / "punjab_rental_dataset.csv"
    )

    df = add_area_category(df)

    print(df[["area", "area_category"]].head(20))

    print("\nCategory Counts:")
    print(df["area_category"].value_counts())