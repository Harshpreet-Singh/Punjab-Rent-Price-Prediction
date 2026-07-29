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
    """
    Extract furnishing status from property title.

    Categories:
    - Fully Furnished
    - Semi Furnished
    - Furnished
    - Unknown
    """

    def get_furnishing(title):

        if pd.isna(title):
            return "Unknown"

        title = title.lower()

        # Check fully furnished first
        fully_furnished_keywords = [
            "fully furnished",
            "full furnished",
            "fully-furnished"
        ]

        for keyword in fully_furnished_keywords:
            if keyword in title:
                return "Fully Furnished"


        # Check semi furnished
        semi_furnished_keywords = [
            "semi furnished",
            "semi-furnished",
            "semi furnished flat",
            "semi furnished floor"
        ]

        for keyword in semi_furnished_keywords:
            if keyword in title:
                return "Semi Furnished"


        # Check generic furnished
        furnished_keywords = [
            " furnished",
            "furnished "
        ]

        for keyword in furnished_keywords:
            if keyword in title:
                return "Furnished"


        return "Unknown"


    df["furnishing"] = df["title"].apply(get_furnishing)

    return df



def extract_property_type(df):
    """
    Extract property type from property title.

    Categories:
    - Apartment
    - Flat
    - Independent House
    - Independent Floor
    - Room Set
    - PG
    - Unknown
    """

    def get_property_type(title):

        if pd.isna(title):
            return "Unknown"

        title = title.lower()

        if "apartment" in title:
            return "Apartment"

        if "flat" in title:
            return "Flat"

        if "independent floor" in title or "floor" in title:
            return "Independent Floor"

        if "independent house" in title or "house" in title:
            return "Independent House"

        if "room set" in title or "roomset" in title:
            return "Room Set"

        if "pg" in title:
            return "PG"

        return "Unknown"

    df["property_type"] = df["title"].apply(get_property_type)

    return df

def create_engineered_features(df):
    """ Apply all feature engineering steps. """

    df = add_area_category(df)
    df = extract_furnishing(df)
    df = extract_property_type(df)

    return df

if __name__ == "__main__":

    from pathlib import Path
    import pandas as pd

    BASE_DIR = Path(__file__).resolve().parent.parent

    df = pd.read_csv(
        BASE_DIR / "data" / "punjab_rental_dataset.csv"
    )


    df = create_engineered_features(df)

    print(df.columns)   