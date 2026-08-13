from pathlib import Path

import joblib
import pandas as pd


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
# Feature Engineering
# ============================================================

def create_area_category(area: float) -> str:
    """Create area category using the same training thresholds."""

    if area <= 750:
        return "Small"

    if area <= 1680:
        return "Medium"

    return "Large"


# ============================================================
# Build Model Input
# ============================================================

def build_input(
    bhk: int,
    bathroom: int,
    area: float,
    location: str,
    city: str,
    furnishing: str,
    property_type: str,
) -> pd.DataFrame:
    """Build a DataFrame matching the model's training features."""

    area_category = create_area_category(area)

    return pd.DataFrame({
        "bhk": [bhk],
        "bathroom": [bathroom],
        "area": [area],
        "location": [location],
        "city": [city],
        "area_category": [area_category],
        "furnishing": [furnishing],
        "property_type": [property_type],
    })


# ============================================================
# Predict Rent
# ============================================================

def predict_rent(
    bhk: int,
    bathroom: int,
    area: float,
    location: str,
    city: str,
    furnishing: str,
    property_type: str,
) -> float:
    """Run the exact KIRA prediction pipeline."""

    input_data = build_input(
        bhk=bhk,
        bathroom=bathroom,
        area=area,
        location=location,
        city=city,
        furnishing=furnishing,
        property_type=property_type,
    )

    transformed_data = preprocessor.transform(
        input_data
    )

    prediction = model.predict(
        transformed_data
    )

    return float(prediction[0])


# ============================================================
# Impact Classification
# ============================================================

def classify_impact(impact: float) -> str:
    """Convert numerical impact into a simple UI-friendly label."""

    absolute_impact = abs(impact)

    if absolute_impact >= 2500:
        return "Strong influence"

    if absolute_impact >= 1000:
        return "Moderate influence"

    return "Small influence"


# ============================================================
# Feature Impact Calculation
# ============================================================

def calculate_feature_impacts(
    bhk: int,
    bathroom: int,
    area: float,
    location: str,
    city: str,
    furnishing: str,
    property_type: str,
) -> list[dict]:
    """
    Estimate local feature impact using controlled
    counterfactual predictions.

    Location is used by the model but is intentionally
    excluded from the local impact ranking because we
    don't currently have a reliable location baseline.

    This is a local model sensitivity measure, not a
    causal explanation.
    """

    original_prediction = predict_rent(
        bhk=bhk,
        bathroom=bathroom,
        area=area,
        location=location,
        city=city,
        furnishing=furnishing,
        property_type=property_type,
    )

    impacts = []

    # ========================================================
    # Area
    # ========================================================

    if area > 200:
        comparison_area = area - 200

        comparison_prediction = predict_rent(
            bhk=bhk,
            bathroom=bathroom,
            area=comparison_area,
            location=location,
            city=city,
            furnishing=furnishing,
            property_type=property_type,
        )

        impact = original_prediction - comparison_prediction

        impacts.append({
            "feature": "Area",
            "value": f"{area:g} sqft",
            "impact": round(impact, 2),
            "influence": classify_impact(impact),
        })

    # ========================================================
    # Bedrooms
    # ========================================================

    if bhk > 1:
        comparison_bhk = bhk - 1

        comparison_prediction = predict_rent(
            bhk=comparison_bhk,
            bathroom=bathroom,
            area=area,
            location=location,
            city=city,
            furnishing=furnishing,
            property_type=property_type,
        )

        impact = original_prediction - comparison_prediction

        impacts.append({
            "feature": "Bedrooms",
            "value": f"{bhk} BHK",
            "impact": round(impact, 2),
            "influence": classify_impact(impact),
        })

    # ========================================================
    # Bathrooms
    # ========================================================

    if bathroom > 1:
        comparison_bathroom = bathroom - 1

        comparison_prediction = predict_rent(
            bhk=bhk,
            bathroom=comparison_bathroom,
            area=area,
            location=location,
            city=city,
            furnishing=furnishing,
            property_type=property_type,
        )

        impact = original_prediction - comparison_prediction

        impacts.append({
            "feature": "Bathrooms",
            "value": str(bathroom),
            "impact": round(impact, 2),
            "influence": classify_impact(impact),
        })

    # ========================================================
    # Furnishing
    # ========================================================

    furnishing_baselines = {
        "Fully Furnished": "Semi Furnished",
        "Semi Furnished": "Fully Furnished",
        "Furnished": "Semi Furnished",
    }

    comparison_furnishing = furnishing_baselines.get(
        furnishing
    )

    if comparison_furnishing:
        comparison_prediction = predict_rent(
            bhk=bhk,
            bathroom=bathroom,
            area=area,
            location=location,
            city=city,
            furnishing=comparison_furnishing,
            property_type=property_type,
        )

        impact = original_prediction - comparison_prediction

        impacts.append({
            "feature": "Furnishing",
            "value": furnishing,
            "impact": round(impact, 2),
            "influence": classify_impact(impact),
        })

    # ========================================================
    # Property Type
    # ========================================================

    property_type_baselines = {
        "Apartment": "Flat",
        "Flat": "Apartment",
        "Independent House": "Independent Floor",
        "Independent Floor": "Independent House",
        "Room Set": "PG",
        "PG": "Room Set",
    }

    comparison_property_type = property_type_baselines.get(
        property_type
    )

    if comparison_property_type:
        comparison_prediction = predict_rent(
            bhk=bhk,
            bathroom=bathroom,
            area=area,
            location=location,
            city=city,
            furnishing=furnishing,
            property_type=comparison_property_type,
        )

        impact = original_prediction - comparison_prediction

        impacts.append({
            "feature": "Property type",
            "value": property_type,
            "impact": round(impact, 2),
            "influence": classify_impact(impact),
        })

    # ========================================================
    # Sort by absolute impact
    # ========================================================

    impacts.sort(
        key=lambda item: abs(item["impact"]),
        reverse=True,
    )

    return impacts