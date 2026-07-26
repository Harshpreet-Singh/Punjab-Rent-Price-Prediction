from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

from preprocessing import preprocess_data
from evaluate_model import calculate_metrics, save_metrics

BASE_DIR = Path(__file__).resolve().parent.parent

MODELS_DIR = BASE_DIR / "models"
METRICS_DIR = BASE_DIR / "outputs" / "metrics"

def load_preprocessed_data():
    pass


def create_param_grid():
    pass


def tune_model():
    pass


def save_model():
    pass


def main():
    pass


if __name__ == "__main__":
    main()