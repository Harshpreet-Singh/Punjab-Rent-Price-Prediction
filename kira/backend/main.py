from pathlib import Path
from typing import Literal

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


# ============================================================
# Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "random_forest_tuned.pkl"
PREPROCESSOR_PATH = BASE_DIR / "models" / "preprocessor.pkl"

DATASET_PATH = BASE_DIR / "data" / "punjab_rental_dataset.csv"


# ============================================================
# Load Rental Dataset
# ============================================================

try:
    rental_data = pd.read_csv(DATASET_PATH)

except Exception as error:
    raise RuntimeError(
        f"Failed to load rental dataset: {error}"
    ) from error

required_columns = {"city", "location"}

missing_columns = required_columns - set(rental_data.columns)

if missing_columns:
    raise RuntimeError(
        f"Dataset is missing required columns: {missing_columns}"
    )

location_map = (
    rental_data[["city", "location"]]
    .dropna()
    .drop_duplicates()
    .groupby("city")["location"]
    .apply(lambda locations: sorted(locations.tolist()))
    .to_dict()
)


# ============================================================
# Load ML Artifacts
# ============================================================

try:
    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)

except Exception as error:
    raise RuntimeError(
        f"Failed to load ML artifacts: {error}"
    ) from error


# ============================================================
# FastAPI Application
# ============================================================

app = FastAPI(
    title="KIRA API",
    description="Punjab Rent Intelligence API",
    version="1.0.0",
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# Request Schema
# ============================================================

class PropertyDetails(BaseModel):
    bhk: int = Field(
        ...,
        ge=1,
        le=10,
        description="Number of bedrooms",
    )

    bathroom: int = Field(
        ...,
        ge=1,
        le=10,
        description="Number of bathrooms",
    )

    area: float = Field(
        ...,
        gt=0,
        le=10000,
        description="Property area in square feet",
    )

    city: str = Field(
        ...,
        min_length=1,
    )

    location: str = Field(
        ...,
        min_length=1,
    )

    furnishing: Literal[
        "Fully Furnished",
        "Semi Furnished",
        "Furnished",
        "Unknown",
    ]

    property_type: Literal[
        "Apartment",
        "Flat",
        "Independent House",
        "Independent Floor",
        "Room Set",
        "PG",
        "Unknown",
    ]


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
# Health Check
# ============================================================

@app.get("/")
def root():
    return {
        "message": "KIRA API is running",
        "status": "ok",
    }


# ============================================================
# Location Endpoint
# ============================================================

@app.get("/locations")
def get_locations():
    """Return available cities and their locations."""

    return {
        "locations": location_map
    }

# ============================================================
# Prediction Endpoint
# ============================================================

@app.post("/predict")
def predict_rent(property_details: PropertyDetails):
    """Predict monthly rent for a property."""

    try:
        area_category = create_area_category(
            property_details.area
        )

        input_data = pd.DataFrame({
            "bhk": [property_details.bhk],
            "bathroom": [property_details.bathroom],
            "area": [property_details.area],
            "location": [property_details.location],
            "city": [property_details.city],
            "area_category": [area_category],
            "furnishing": [property_details.furnishing],
            "property_type": [property_details.property_type],
        })

        transformed_data = preprocessor.transform(
            input_data
        )

        prediction = model.predict(
            transformed_data
        )

        predicted_rent = float(prediction[0])

        return {
            "predicted_rent": round(
                predicted_rent,
                2,
            )
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Please try again.",
        ) from error