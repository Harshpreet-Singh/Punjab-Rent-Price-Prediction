"""
train_lightgbm.py

Purpose:
Train and evaluate a LightGBM Regressor.
"""

from pathlib import Path

import joblib
from lightgbm import LGBMRegressor

from ml.evaluate_model import calculate_metrics, save_metrics
from ml.preprocessing import preprocess_data

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "lightgbm.pkl"

METRICS_PATH = (
    BASE_DIR
    / "outputs"
    / "metrics"
    / "lightgbm_metrics.txt"
)