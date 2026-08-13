from pathlib import Path

import joblib
import pandas as pd
import shap


# ============================================================
# Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = BASE_DIR / "models" / "random_forest_tuned.pkl"
PREPROCESSOR_PATH = BASE_DIR / "models" / "preprocessor.pkl"


# ============================================================
# Load ML Artifacts
# ============================================================

model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)


# ============================================================
# Sample Property
# ============================================================

area = 1200

if area <= 750:
    area_category = "Small"

elif area <= 1680:
    area_category = "Medium"

else:
    area_category = "Large"


input_data = pd.DataFrame({
    "bhk": [2],
    "bathroom": [2],
    "area": [area],
    "location": ["Sector 70"],
    "city": ["Mohali"],
    "area_category": [area_category],
    "furnishing": ["Semi Furnished"],
    "property_type": ["Apartment"],
})


# ============================================================
# Transform Input
# ============================================================

transformed_data = preprocessor.transform(
    input_data
)

# SHAP TreeExplainer works better with dense numeric data.
# The KIRA input contains only 530 transformed features,
# so converting this single row to dense is lightweight.

transformed_data_dense = transformed_data.toarray()


# ============================================================
# Feature Names
# ============================================================

feature_names = preprocessor.get_feature_names_out()


# ============================================================
# SHAP Explanation
# ============================================================

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(
    transformed_data_dense,
    check_additivity=False,
)


# ============================================================
# SHAP Contributions
# ============================================================

contributions = pd.DataFrame({
    "feature": feature_names,
    "shap_value": shap_values[0],
})

contributions["absolute_impact"] = (
    contributions["shap_value"].abs()
)

contributions = contributions.sort_values(
    "absolute_impact",
    ascending=False,
)


# ============================================================
# Display Results
# ============================================================

print("\n" + "=" * 60)
print("TOP SHAP CONTRIBUTIONS")
print("=" * 60)

print(
    contributions[
        ["feature", "shap_value"]
    ].head(15).to_string(index=False)
)


print("\n" + "=" * 60)
print("PREPROCESSOR STRUCTURE")
print("=" * 60)

print(preprocessor)