from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor

from preprocessing import preprocess_data
from evaluate_model import calculate_metrics

BASE_DIR = Path(__file__).resolve().parent.parent

METRICS_DIR = BASE_DIR / "outputs" / "metrics"
FIGURES_DIR = BASE_DIR / "outputs" / "figures"


def create_experiments():
    """Define feature combinations for the ablation study."""

    return {
        "Baseline": [
            "bhk",
            "bathroom",
            "area",
            "location",
            "city",
        ],

        "Area Category": [
            "bhk",
            "bathroom",
            "area",
            "location",
            "city",
            "area_category",
        ],

        "Furnishing": [
            "bhk",
            "bathroom",
            "area",
            "location",
            "city",
            "furnishing",
        ],

        "Property Type": [
            "bhk",
            "bathroom",
            "area",
            "location",
            "city",
            "property_type",
        ],

        "All Features": [
            "bhk",
            "bathroom",
            "area",
            "location",
            "city",
            "area_category",
            "furnishing",
            "property_type",
        ],
    }

def train_experiment(features):
    """Train and evaluate one feature combination."""

    (
        X_train,
        X_test,
        y_train,
        y_test,
        _,
    ) = preprocess_data(features)

    model = RandomForestRegressor(
        random_state=42,
        n_estimators=200,
    )

    model.fit(
        X_train,
        y_train,
    )

    metrics = calculate_metrics(
        model,
        X_test,
        y_test,
        "",
    )

    return metrics

def run_ablation_study(experiments):
    """Run every experiment."""

    results = []

    for name, features in experiments.items():

        print(f"\nRunning: {name}")

        metrics = train_experiment(features)

        metrics["Model"] = name

        results.append(metrics)

    results_df = pd.DataFrame(results)

    results_df = results_df.sort_values(
        by="R2",
        ascending=False,
    )

    return results_df   

def save_results(results):
    """Save ablation study results."""

    METRICS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    results.to_csv(
        METRICS_DIR / "ablation_study.csv",
        index=False,
    )
def plot_ablation_study(results):
    """Create a bar chart comparing the R² score of each experiment."""

    FIGURES_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    plot_df = results.sort_values(
        by="R2",
        ascending=False,
    )

    plt.figure(figsize=(9, 5))

    bars = plt.bar(
        plot_df["Model"],
        plot_df["R2"],
    )

    for bar in bars:
        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.0008,
            f"{height:.3f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.title("Ablation Study (R² Comparison)")

    plt.xlabel("Experiment")

    plt.ylabel("R² Score")

    plt.ylim(0.85, 0.93)

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.4,
    )

    plt.xticks(rotation=15)

    plt.tight_layout()

    plt.savefig(
        FIGURES_DIR / "ablation_study.png",
        dpi=300,
    )

    plt.close()

def print_results(results):
    """Display ablation study results."""

    print("\n========== Ablation Study ==========\n")

    print(
        results[
            [
                "Model",
                "MAE",
                "RMSE",
                "R2",
            ]
        ]
    )


def main():

    experiments = create_experiments()

    results = run_ablation_study(
        experiments,
    )

    save_results(results)

    plot_ablation_study(results)

    print_results(results)


if __name__ == "__main__":
    main()