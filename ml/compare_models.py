"""
compare_models.py

Linear Regression
        │
        ▼
evaluate()
        │
        ▼
Metrics
        │
        ▼
Decision Tree
        │
        ▼
evaluate()
        │
        ▼
Metrics
        │
        ▼
Random Forest
        │
        ▼
evaluate()
        │
        ▼
Metrics
        │
        ▼
Create DataFrame
        │
        ▼
Sort by R²
        │
        ▼
Save CSV

Compare all trained machine learning models.
"""

from pathlib import Path

import pandas as pd

from evaluate_model import evaluate


OUTPUT_DIR = Path("./outputs/metrics")

MODELS = [
    "linear_regression",
    "decision_tree",
    "random_forest",
]


def compare_models():
    """
    Evaluate all models and compare their performance.
    """

    results = []

    print("=" * 50)
    print("Comparing Machine Learning Models")
    print("=" * 50)

    for model_name in MODELS:

        print(f"\nEvaluating: {model_name.replace('_', ' ').title()}")

        metrics = evaluate(model_name, verbose=False)

        results.append(metrics)

    comparison_df = pd.DataFrame(results)

    comparison_df = comparison_df.sort_values(   # Highest R² appears first.
        by="R2",
        ascending=False
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_path = OUTPUT_DIR / "model_comparison.csv"

    comparison_df.to_csv(output_path, index=False)

    print("\n" + "=" * 50)
    print("Final Model Comparison")
    print("=" * 50)

    print(comparison_df)

    print(f"\nComparison saved to: {output_path}")


def main():

    compare_models()


if __name__ == "__main__":
    main()