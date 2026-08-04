from pathlib import Path

import joblib
from sklearn.ensemble import GradientBoostingRegressor

from ml.evaluate_model import calculate_metrics, save_metrics
from ml.preprocessing import preprocess_data

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "gradient_boosting.pkl"

METRICS_PATH = (
    BASE_DIR
    / "outputs"
    / "metrics"
    / "gradient_boosting_metrics.txt"
)