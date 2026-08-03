from pathlib import Path

import joblib
import shap
import matplotlib.pyplot as plt

from preprocessing import (
    preprocess_data,
    DEFAULT_FEATURES,
)
BASE_DIR = Path(__file__).resolve().parent.parent

MODELS_DIR = BASE_DIR / "models"

FIGURES_DIR = BASE_DIR / "outputs" / "figures"

def load_artifacts():
    """Load trained model and fitted preprocessor."""

    model = joblib.load(
        MODELS_DIR / "random_forest_tuned.pkl"
    )

    preprocessor = joblib.load(
        MODELS_DIR / "preprocessor.pkl"
    )

    return model, preprocessor



def load_data():
    """Load encoded test data."""

    (
        _,
        X_test,
        _,
        _,
        _,
    ) = preprocess_data(DEFAULT_FEATURES)

    return X_test

def create_explainer(model):
    """Create SHAP TreeExplainer."""

    return shap.TreeExplainer(model)

def calculate_shap_values(
    explainer,
    X_test,
):
    """Calculate SHAP values."""

    return explainer(X_test)

def save_summary_plot(shap_values):
    """Save SHAP summary plot."""

    FIGURES_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.figure()

    shap.plots.beeswarm(
        shap_values,
        max_display=20,
        show=False,
    )

    plt.tight_layout()

    plt.savefig(
        FIGURES_DIR / "shap_summary.png",
        dpi=300,
    )

    plt.close()

def save_bar_plot(shap_values):
    """Save SHAP bar plot."""

    plt.figure()

    shap.plots.bar(
        shap_values,
        max_display=20,
        show=False,
    )

    plt.tight_layout()

    plt.savefig(
        FIGURES_DIR / "shap_bar.png",
        dpi=300,
    )

    plt.close()


def save_waterfall_plot(shap_values):
    """Save SHAP waterfall plot."""

    shap.plots.waterfall(
        shap_values[0],
        max_display=20,
        show=False,
    )

    plt.savefig(
        FIGURES_DIR / "shap_waterfall.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()

def main():

    model, _ = load_artifacts()

    FIGURES_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    X_test = load_data()
    
    X_test = X_test.toarray()
    X_test = X_test[:500]
    print(type(X_test))
    print(X_test.shape)

    explainer = create_explainer(model)

    shap_values = calculate_shap_values(
        explainer,
        X_test,
    )

    save_summary_plot(
        shap_values,
    )

    save_bar_plot(
        shap_values,
    )

    save_waterfall_plot(
        shap_values,
    )

    print("\nSHAP plots saved successfully.")


if __name__ == "__main__":
    main()