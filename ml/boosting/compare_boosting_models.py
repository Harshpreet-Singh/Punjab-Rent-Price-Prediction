"""
Models that are going to be compared in this file:
Gradient Boosting
Gradient Boosting Tuned

XGBoost
XGBoost Tuned

Random Forest
Random Forest Tuned
"""

from pathlib import Path

import pandas as pd

from ml.evaluate_model import evaluate

BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_PATH = (
    BASE_DIR
    / "outputs"
    / "metrics"
    / "boosting_model_comparison.csv"
)

def get_boosting_models():
    """Return the boosting models to compare."""

    return [
        "gradient_boosting",
        "gradient_boosting_tuned",
        "xgboost",
        "xgboost_tuned",
        "random_forest",
        "random_forest_tuned",
    ]
def main():

    # Load models
    results = []

    # Evaluate
    for model_name in get_boosting_models():

        metrics = evaluate(
            model_name,
            verbose=False,
        )

        results.append(metrics)

    # Create DataFrame
    comparison_df = pd.DataFrame(results)

    # Sort
    comparison_df = comparison_df.sort_values(
        by="R2",
        ascending=False,
    ).reset_index(drop=True) # Reset Index

    # Round
    comparison_df = comparison_df.round(
        {
            "MAE": 2,
            "MSE": 2,
            "RMSE": 2,
            "R2": 4,
        }
    )

    # ensure output dir exists 
    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    comparison_df.to_csv(
        OUTPUT_PATH,
        index=False,
    )
    print("\n========== Boosting Model Comparison ==========\n")

    print(comparison_df)

    comparison_df.to_csv(
        OUTPUT_PATH,
        index=False,
    )

    print(f"\nComparison saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()