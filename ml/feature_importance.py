import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODELS_DIR = BASE_DIR / "models"
OUTPUTS_DIR = BASE_DIR / "outputs" / "metrics"

model = joblib.load(MODELS_DIR / "random_forest_tuned.pkl")
preprocessor = joblib.load(MODELS_DIR / "preprocessor.pkl")

feature_names = preprocessor.get_feature_names_out()
importance = model.feature_importances_

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

importance_df.to_csv(
    OUTPUTS_DIR / "feature_importance.csv",
    index=False
)

print("\nTop 20 Important Features\n")
print(importance_df.head(20))