<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn" />
  <img src="https://img.shields.io/badge/Random%20Forest-Best%20Model-9ACD32?style=for-the-badge" alt="Random Forest" />
  <img src="https://img.shields.io/badge/XGBoost-ML-189FDD?style=for-the-badge" alt="XGBoost" />
  <img src="https://img.shields.io/badge/LightGBM-ML-9ACD32?style=for-the-badge" alt="LightGBM" />
  <img src="https://img.shields.io/badge/React-Vite-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React" />
  <img src="https://img.shields.io/badge/Tailwind%20CSS-UI-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Status-Portfolio%20Ready-success?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/Best%20R²-0.9156-brightgreen?style=for-the-badge" alt="Best R2" />
</p>

<h1 align="center">Punjab Rent Price Prediction</h1>

<p align="center">
  <strong>KIRA — Punjab Rent Intelligence</strong>
</p>

<p align="center">
  An end-to-end Machine Learning project that turns real-world Punjab rental listings into rent estimates, model insights, and an interactive web prediction experience.
</p>

---

## Overview

**Punjab Rent Price Prediction** is an end-to-end Machine Learning project built around real rental listings collected from OLX for locations across Punjab.

The project started as a learning-focused ML workflow and evolved into **KIRA (Punjab Rent Intelligence)** — a user-facing prediction application built around the trained rental-price model.

The project covers the complete pipeline:

```text
Real-world Rental Data
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Preprocessing
        ↓
Model Training
        ↓
Hyperparameter Tuning
        ↓
Model Evaluation
        ↓
Explainability
        ↓
Prediction API
        ↓
KIRA Web Application
```

The goal is not only to predict rent, but also to make the prediction understandable through expected rental ranges and a human-readable **KIRA'S TAKE** Smart Verdict.

---

# KIRA

## Punjab Rent Intelligence

KIRA is the web-facing layer of the project.

Instead of requiring users to interact with a Python command-line program, KIRA provides a clean interface where users can describe a rental property and receive an estimated monthly rent.

### KIRA currently provides

- Property-based rent prediction
- City and location selection
- Bedrooms and bathroom inputs
- Area input
- Furnishing selection
- Property type selection
- Estimated monthly rent
- Expected rental range
- Feature-impact explanation
- **KIRA'S TAKE** Smart Verdict
- Property summary after prediction

The application is designed around a simple principle:

> **Know your rent before you move.**

---

# Project Objective

The primary objective is to build a practical rental-price prediction system while learning and implementing the complete Machine Learning lifecycle.

### Core objectives

- Build a rental price prediction model using real-world data.
- Understand the complete Machine Learning workflow.
- Clean and prepare scraped rental listings.
- Engineer meaningful rental-property features.
- Train and compare multiple regression algorithms.
- Tune promising models using hyperparameter search.
- Evaluate models using standard regression metrics.
- Analyze feature importance and model behaviour.
- Build a reusable preprocessing and prediction pipeline.
- Expose the trained model through a backend API.
- Build a user-facing web application around the model.
- Present model predictions in a clear and understandable way.

---

# Dataset

The project uses rental property listings collected from **OLX** for three major locations in Punjab:

- SAS Nagar
- Mohali
- Kharar

### Dataset size

**13,877 rental listings**

### Target variable

```text
price
```

The target represents the monthly rental price of a property.

---

# Data Cleaning

The raw scraped listings required substantial preprocessing before they could be used for Machine Learning.

Major cleaning operations included:

- Removing unnecessary URL information.
- Extracting BHK information.
- Extracting bathroom information.
- Extracting property area.
- Converting rental prices into numerical values.
- Standardizing BHK representations.
- Removing sale listings.
- Handling invalid area values.
- Removing unrealistic and extreme listings.
- Removing duplicate records.
- Cleaning location and property information.
- Merging the cleaned regional datasets.

The final merged dataset is stored at:

```text
data/punjab_rental_dataset.csv
```

---

# Feature Engineering

Feature engineering was used to convert raw listing information into features suitable for the prediction pipeline.

## Core Features

- `bhk`
- `bathroom`
- `area`
- `location`
- `city`

## Engineered Features

### Area Category

Properties are grouped into area categories:

- Small
- Medium
- Large

### Furnishing

Furnishing information is extracted and standardized into categories such as:

- Fully Furnished
- Semi Furnished
- Furnished
- Unknown

### Property Type

Property information is extracted and standardized into categories such as:

- Apartment
- Flat
- Independent House
- Independent Floor
- Room Set
- PG
- Unknown

These engineered features are passed through the same preprocessing pipeline used during model training and prediction.

---

# Machine Learning Workflow

```text
Raw OLX Listings
       │
       ▼
Data Cleaning
       │
       ▼
Dataset Merging
       │
       ▼
Feature Engineering
       │
       ▼
Feature Selection
       │
       ▼
Train / Test Split
       │
       ▼
Preprocessing
       │
       ▼
Model Training
       │
       ▼
Hyperparameter Tuning
       │
       ▼
Model Evaluation
       │
       ▼
Model Comparison
       │
       ▼
Best Model Selection
       │
       ▼
Prediction Pipeline
       │
       ▼
FastAPI Backend
       │
       ▼
KIRA Web Application
```

---

# Models Implemented

The project contains **10 model configurations** across traditional regression and boosting algorithms.

### Traditional Regression

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Tuned Random Forest Regressor

### Boosting

- Gradient Boosting Regressor
- Tuned Gradient Boosting Regressor
- XGBoost
- Tuned XGBoost
- LightGBM
- Tuned LightGBM

Selected models were tuned using **GridSearchCV**.

---

# Model Comparison

The current model comparison is based on the project's generated metrics:

`outputs/metrics/model_comparison.csv`

| Rank | Model                   |           MAE |          RMSE |         R² |
| ---: | ----------------------- | ------------: | ------------: | ---------: |
|    1 | **Random Forest Tuned** | **₹2,409.65** | **₹3,925.13** | **0.9156** |
|    2 | Random Forest           |     ₹2,415.63 |     ₹3,968.82 |     0.9137 |
|    3 | XGBoost                 |     ₹4,294.77 |     ₹5,965.17 |     0.8051 |
|    4 | LightGBM Tuned          |     ₹4,089.56 |     ₹5,966.82 |     0.8050 |
|    5 | Gradient Boosting Tuned |     ₹4,723.17 |     ₹6,477.87 |     0.7702 |
|    6 | XGBoost Tuned           |     ₹4,787.48 |     ₹6,643.71 |     0.7582 |
|    7 | LightGBM                |     ₹4,738.98 |     ₹6,936.62 |     0.7365 |
|    8 | Linear Regression       |     ₹5,235.75 |     ₹7,645.27 |     0.6799 |
|    9 | Gradient Boosting       |     ₹5,579.91 |     ₹7,880.15 |     0.6599 |
|   10 | Decision Tree           |     ₹6,253.57 |     ₹8,946.48 |     0.5616 |

> **Note:** These values are from the project's current `outputs/metrics/model_comparison.csv`.

---

# Best Model

## Tuned Random Forest Regressor

The current best-performing model is the tuned Random Forest Regressor.

### Performance

| Metric   |             Value |
| -------- | ----------------: |
| **MAE**  |     **₹2,409.65** |
| **MSE**  | **15,406,626.23** |
| **RMSE** |     **₹3,925.13** |
| **R²**   |        **0.9156** |

An R² score of **0.9156** means that the model explains approximately **91.56% of the variance** in rental prices on the evaluated test set.

The trained model is stored at:

```text
models/random_forest_tuned.pkl
```

---

# Evaluation Metrics

The models are evaluated using standard regression metrics.

### MAE — Mean Absolute Error

Average absolute difference between actual and predicted rent.

**Lower is better.**

### MSE — Mean Squared Error

Squares prediction errors, giving larger errors greater weight.

**Lower is better.**

### RMSE — Root Mean Squared Error

Measures prediction error in the same unit as rental price.

**Lower is better.**

### R² — R-Squared

Measures the proportion of variance in rental prices explained by the model.

**Higher is better.**

---

# Model Explainability

The project includes multiple tools for understanding model behaviour.

Current analysis includes:

- Feature Importance
- Grouped Feature Importance
- Ablation Study
- Cross Validation
- SHAP Analysis
- Prediction-level feature impacts

Generated analysis outputs include:

```text
outputs/figures/
├── ablation_study.png
├── feature_importance.png
├── shap_bar.png
├── shap_summary.png
└── shap_waterfall.png
```

These analyses help answer not only:

> **"What rent did the model predict?"**

but also:

> **"Which property characteristics influenced the prediction?"**

---

# KIRA Smart Verdict

KIRA includes a lightweight interpretation layer called **Smart Verdict**.

After a prediction is generated, KIRA uses the model's existing prediction information to create a short human-readable interpretation.

### Smart Verdict uses

- Predicted rent
- Expected rental range
- Feature impacts
- Impact direction
- Impact strength

### Example

For a property where:

```text
Predicted rent: ₹21,259
Expected range: ₹13,000 – ₹33,000

Bedrooms:    +₹3,494
Furnishing:  -₹5,967
Area:        +₹1,407
Property:    +₹455
Bathrooms:   +₹150
```

KIRA can generate:

> **Your estimate sits around the middle of KIRA's expected rental range.**

> **Bedrooms have a strong positive influence on KIRA's prediction. Furnishing has a strong downward influence on KIRA's prediction.**

The Smart Verdict is intentionally described as **model interpretation**, not causal analysis.

For example, KIRA says:

> "Bedrooms have a strong positive influence on KIRA's prediction."

rather than claiming:

> "Adding a bedroom increases rent by ₹3,494."

This distinction is important because feature impact represents model sensitivity, not a causal real-world effect.

---

# Prediction System

The original reusable command-line prediction system is available at:

```text
ml/predict.py
```

It:

1. Loads the trained model.
2. Loads the fitted preprocessing pipeline.
3. Accepts property information.
4. Generates required engineered features.
5. Applies the same preprocessing used during training.
6. Produces the estimated monthly rent.

### Example

```text
BHK: 3
Bathroom: 2
Area: 1500 sqft
Location: Phase 7
City: SAS Nagar

Furnishing:
2. Semi Furnished

Property Type:
2. Flat
```

Example:

```text
========== Prediction ==========

Estimated Monthly Rent: ₹20,557.97
```

---

# Backend API

The project has been extended from a command-line prediction workflow into a web-ready prediction system.

The backend exposes the trained model through an API.

The prediction flow is:

```text
KIRA Frontend
      ↓
Rent Form
      ↓
API Request
      ↓
FastAPI Backend
      ↓
Preprocessing Pipeline
      ↓
Tuned Random Forest
      ↓
Prediction + Range + Feature Impacts
      ↓
KIRA Frontend
```

The API response provides the frontend with the information required to render:

- Estimated rent
- Expected rental range
- Feature impacts
- Property summary
- Smart Verdict

---

# Web Application

## KIRA — Punjab Rent Intelligence

The frontend is built using:

- React
- Vite
- Tailwind CSS
- JavaScript

KIRA focuses on a clean, minimal and user-friendly rental estimation experience.

### Frontend flow

```text
Landing Page
    ↓
How KIRA Works
    ↓
Property Input Form
    ↓
Prediction
    ↓
Estimated Rent
    ↓
Expected Rental Range
    ↓
KIRA'S TAKE
    ↓
Feature Impacts
    ↓
Property Summary
```

The interface avoids unnecessary complexity and presents the prediction in a way that is understandable even to users without Machine Learning knowledge.

---

# Power BI Dashboard

Before building the Machine Learning pipeline, the rental dataset was explored using **Power BI**.

The dashboard was used to understand:

- Rental price patterns
- BHK distribution
- Location-wise rental prices
- Property trends
- Dataset-level business insights

This analysis helped establish an understanding of the rental market before model development.

---

# Project Structure

```text
Punjab-Rent-Price-Prediction/
│
├── data/
│   ├── kharar_cleaned_data.csv
│   ├── mohali_cleaned_data.csv
│   ├── punjab_rental_dataset.csv
│   └── sas_cleaned_data.csv
│
├── data_cleaning/
│   ├── kharar_data_cleaning.py
│   ├── mohali_data_cleaning.py
│   ├── sas_data_cleaning.py
│   └── merge_data.py
│
├── ml/
│   ├── ablation_study.py
│   ├── compare_models.py
│   ├── cross_validation.py
│   ├── evaluate_model.py
│   ├── feature_engineering.py
│   ├── feature_importance.py
│   ├── inspect_area.py
│   ├── inspect_title.py
│   ├── predict.py
│   ├── preprocessing.py
│   ├── shap_explain.py
│   ├── train_decision_tree.py
│   ├── train_linear_regression.py
│   ├── train_random_forest.py
│   ├── tune_random_forest.py
│   │
│   ├── boosting/
│   │   ├── compare_boosting_models.py
│   │   ├── train_gradient_boosting.py
│   │   └── tune_gradient_boosting.py
│   │
│   ├── lightgbm/
│   │   ├── train_lightgbm.py
│   │   └── tune_lightgbm.py
│   │
│   └── xgboost/
│       ├── train_xgboost.py
│       └── tune_xgboost.py
│
├── models/
│   ├── decision_tree.pkl
│   ├── gradient_boosting.pkl
│   ├── gradient_boosting_tuned.pkl
│   ├── lightgbm.pkl
│   ├── lightgbm_tuned.pkl
│   ├── linear_regression.pkl
│   ├── preprocessor.pkl
│   ├── random_forest.pkl
│   ├── random_forest_tuned.pkl
│   ├── xgboost.pkl
│   └── xgboost_tuned.pkl
│
├── outputs/
│   ├── figures/
│   ├── metrics/
│   └── predictions/
│
├── kira/
│   ├── backend/
│   └── frontend/
│
├── insights.md
├── notes.md
├── requirements.txt
├── README.md
└── .gitignore
```

> The KIRA folder contains the web application layer. The exact frontend/backend file structure may evolve as the application is developed.

---

# Tech Stack

### Data & Programming

- Python
- Pandas
- NumPy

### Machine Learning

- Scikit-learn
- XGBoost
- LightGBM
- Joblib

### Explainability & Visualization

- Matplotlib
- Seaborn
- SHAP

### Backend

- FastAPI
- Python

### Frontend

- React
- Vite
- Tailwind CSS
- JavaScript

### Business Intelligence

- Power BI

### Development

- Git
- GitHub

---

# Running the ML Prediction System

Clone the repository and install the required dependencies.

```bash
pip install -r requirements.txt
```

Then run:

```bash
py -m ml.predict
```

The command-line system will request the required property details and return an estimated monthly rental price.

---

# Running KIRA

The KIRA application contains separate frontend and backend components.

### Backend

From the backend directory, start the FastAPI application using the project's configured backend entry point.

### Frontend

From the frontend directory:

```bash
npm install
npm run dev
```

> Refer to the current project files for the exact backend entry point and environment configuration.

---

# Project Status

## Machine Learning

- [x] Data Collection
- [x] Data Cleaning
- [x] Dataset Merging
- [x] Exploratory Data Analysis
- [x] Feature Engineering
- [x] Preprocessing
- [x] Linear Regression
- [x] Decision Tree
- [x] Random Forest
- [x] Random Forest Tuning
- [x] Gradient Boosting
- [x] Gradient Boosting Tuning
- [x] XGBoost
- [x] XGBoost Tuning
- [x] LightGBM
- [x] LightGBM Tuning
- [x] Model Evaluation
- [x] Cross Validation
- [x] Model Comparison
- [x] Feature Importance
- [x] Ablation Study
- [x] SHAP Explainability
- [x] Reusable Prediction Pipeline

## KIRA Application

- [x] Frontend foundation
- [x] Property input form
- [x] Prediction API integration
- [x] Rent prediction result
- [x] Expected rental range
- [x] Feature impact display
- [x] Property summary
- [x] KIRA Smart Verdict
- [x] Responsive UI
- [x] Prediction result UX

---

# What This Project Demonstrates

This project brings together several stages of practical Machine Learning development:

### Data Engineering

Working with messy real-world scraped rental data and converting it into a usable dataset.

### Feature Engineering

Extracting meaningful property characteristics from semi-structured listing information.

### Model Development

Training, comparing and tuning multiple regression algorithms instead of relying on a single model.

### Model Evaluation

Using MAE, MSE, RMSE and R² to compare model performance.

### Explainability

Using feature importance, SHAP and prediction-level impacts to understand model behaviour.

### Software Engineering

Keeping data cleaning, ML training, preprocessing, prediction and application code modular.

### Deployment-Oriented Thinking

Connecting the trained ML pipeline to an API and building a user-facing application around it.

---

# Limitations

The model is trained on a dataset collected from online rental listings and therefore reflects the patterns and limitations of that dataset.

Important considerations:

- Rental prices can change over time.
- Listing prices may differ from final negotiated rents.
- Some locations may have more data than others.
- Online listings can contain missing or noisy information.
- The model should be treated as an estimation tool rather than a guaranteed market price.
- The expected rental range represents model prediction variation, not a statistical confidence interval.

---

# Future Improvements

Potential future improvements include:

- Larger and more frequently updated rental datasets.
- Automated data refresh and model retraining.
- Additional geographic coverage across Punjab and other regions.
- Improved location-level features.
- More extensive model validation.
- Model monitoring after deployment.
- Cloud deployment.
- Automated CI/CD.
- Additional model experimentation such as CatBoost.
- More advanced prediction uncertainty estimation.

---

# Learning Journey

This project was built as a practical way to learn Machine Learning from the ground up.

Instead of treating Machine Learning as only model training, the project explores the complete lifecycle:

```text
Data
 ↓
Understanding
 ↓
Cleaning
 ↓
Feature Engineering
 ↓
Model Development
 ↓
Evaluation
 ↓
Explainability
 ↓
API
 ↓
Application
```

The emphasis throughout the project is on understanding **why** each step is performed, while maintaining a modular and portfolio-quality codebase.

---

# Author

**Harshpreet Singh**

B.Tech Computer Science student building practical projects while learning Machine Learning, Data Analysis and full-stack development.

---

# Project Goal

> **Turn real-world Punjab rental data into a practical, explainable and user-friendly rental price prediction system.**

**Punjab Rent Price Prediction** is the Machine Learning foundation.

**KIRA** is the application built on top of it.

Together, they transform a raw rental dataset into an end-to-end prediction product.
