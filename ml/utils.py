"""
utils.py

Common helper functions used across the project.
"""

FEATURE_GROUPS = {
    "area_category": "Area Category",
    "property_type": "Property Type",
    "furnishing": "Furnishing",
    "location": "Location",
    "bathroom": "Bathroom",
    "city": "City",
    "area": "Area",
    "bhk": "BHK",
}


def clean_feature_names(feature_names):
    """
    Clean encoded feature names produced by ColumnTransformer.

    Example:
        categorical__location_Phase 7
            -> location_Phase 7

        remainder__bhk
            -> BHK
    """

    cleaned_names = []

    for feature in feature_names:

        feature = (
            feature
            .replace("categorical__", "")
            .replace("remainder__", "")
        )

        if feature == "bhk":
            feature = "BHK"

        elif feature == "bathroom":
            feature = "Bathroom"

        elif feature == "area":
            feature = "Area"

        elif feature == "city":
            feature = "City"

        elif feature.startswith("location_"):
            feature = feature.replace(
                "location_",
                "",
            )

        elif feature.startswith("furnishing_"):
            feature = feature.replace(
                "furnishing_",
                "",
            )

        elif feature.startswith("property_type_"):
            feature = feature.replace(
                "property_type_",
                "",
            )

        elif feature.startswith("area_category_"):
            feature = feature.replace(
                "area_category_",
                "",
            )

        cleaned_names.append(feature)

    return cleaned_names