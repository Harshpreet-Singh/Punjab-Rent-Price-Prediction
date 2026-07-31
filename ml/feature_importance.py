"""
Final Structure
main()

│
├── load_artifacts()
│
├── extract_feature_importance()
│
├── save_raw_importance()
│
├── group_feature_importance()
│
├── save_grouped_importance()
│
├── plot_feature_importance()
│
└── print_summary()
"""

from pathlib import Path

import joblib
import pandas as pd
import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent.parent

MODELS_DIR = BASE_DIR / "models"

METRICS_DIR = BASE_DIR / "outputs" / "metrics"

FIGURES_DIR = BASE_DIR / "outputs" / "figures"

METRICS_DIR.mkdir(parents=True, exist_ok=True)

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



def load_artifacts():
    """Load the trained model and fitted preprocessor."""

    model = joblib.load(
        MODELS_DIR / "random_forest_tuned.pkl"
    )

    preprocessor = joblib.load(
        MODELS_DIR / "preprocessor.pkl"
    )

    return model, preprocessor


def extract_feature_importance(model, preprocessor):
    """Extract raw feature importance."""

    feature_names = preprocessor.get_feature_names_out()

    importance = model.feature_importances_

    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importance,
    })

    return importance_df.sort_values(
        by="Importance",
        ascending=False,
    )


def clean_feature_names(df):
    """Remove ColumnTransformer prefixes."""

    df = df.copy()

    df["Feature"] = (
        df["Feature"]
        .str.replace("categorical__", "", regex=False)
        .str.replace("remainder__", "", regex=False)
    )

    return df

def group_feature_importance(df):
    """Group encoded features back to original features."""

    grouped_features = []

    for feature in df["Feature"]:

        original_feature = feature

        for prefix, name in FEATURE_GROUPS.items():

            if feature.startswith(prefix):

                original_feature = name
                break

        grouped_features.append(original_feature)

    grouped_df = df.copy()

    grouped_df["Feature"] = grouped_features

    grouped_df = (
        grouped_df
        .groupby("Feature", as_index=False)["Importance"]
        .sum()
        .sort_values(
            by="Importance",
            ascending=False,
        )
    )

    return grouped_df

def save_feature_importance(df, filename):
    """Save feature importance."""

    METRICS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        METRICS_DIR / filename,
        index=False,
    )



def plot_feature_importance(df):
    """Create feature importance plot."""

    FIGURES_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.figure(figsize=(8, 5))

    plt.barh(
        df["Feature"],
        df["Importance"],
    )

    plt.xlabel("Importance")

    plt.title("Feature Importance")

    plt.gca().invert_yaxis()

    plt.tight_layout()

    plt.savefig(
        FIGURES_DIR / "feature_importance.png",
        dpi=300,
    )

    plt.close()

def print_summary(raw_df, grouped_df):
    """Display raw and grouped feature importance."""

    print("\nTop 20 Encoded Features\n")

    print(raw_df.head(20))

    print("\nGrouped Feature Importance\n")

    print(grouped_df)

def main():

    model, preprocessor = load_artifacts()

    raw_df = extract_feature_importance(
        model,
        preprocessor,
    )

    raw_df = clean_feature_names(raw_df)

    grouped_df = group_feature_importance(raw_df)

    save_feature_importance(
        raw_df,
        "feature_importance.csv",
    )

    save_feature_importance(
        grouped_df,
        "feature_importance_grouped.csv",
    )

    plot_feature_importance(grouped_df)

    print_summary(
        raw_df,
        grouped_df,
    )


if __name__ == "__main__":
    main()