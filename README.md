<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn" />
  <img src="https://img.shields.io/badge/XGBoost-ML-189FDD?style=for-the-badge" alt="XGBoost" />
  <img src="https://img.shields.io/badge/LightGBM-ML-9ACD32?style=for-the-badge" alt="LightGBM" />
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-In%20Development-blue?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/Best%20R²-0.9156-brightgreen?style=for-the-badge" alt="Best R2" />
</p>

# Punjab Rent Price Prediction

A Machine Learning project that predicts rental property prices using real-world rental listings collected from OLX for cities in Punjab.

The project follows an end-to-end Machine Learning workflow — from data collection and cleaning to feature engineering, model training, hyperparameter tuning, evaluation, model comparison, and an interactive prediction system.

The project is being developed as a **learning-focused but production-style modular ML codebase**, with the eventual goal of providing a convenient web interface for rent prediction.

---

## Project Objective

The main goal of this project is to learn and implement Machine Learning from scratch while building a practical real-world application.

### Objectives

* Build a rental price prediction model using real-world data.
* Understand the complete Machine Learning workflow.
* Perform data cleaning and preprocessing.
* Apply meaningful Feature Engineering.
* Train and compare multiple regression algorithms.
* Perform hyperparameter tuning.
* Evaluate models using standard regression metrics.
* Analyze feature importance and model explainability.
* Build a reusable prediction pipeline.
* Follow modular and clean software engineering practices.
* Eventually provide an easy-to-use web interface for predictions.

---

## Dataset

The dataset consists of rental property listings collected from **OLX** for three locations in Punjab:

* SAS Nagar
* Mohali
* Kharar

### Dataset Size

**13,877 rental listings**

### Target Variable

```text
price
```

The target represents the rental price of the property.

---

## Data Cleaning

The raw rental listings were cleaned and prepared before Machine Learning.

Major cleaning steps included:

* Removing unnecessary URL information.
* Extracting BHK, bathroom and area information.
* Converting price values into numerical format.
* Standardizing BHK values.
* Removing sale listings.
* Handling invalid area values.
* Removing unrealistic/outlier listings.
* Removing duplicate listings.
* Cleaning and merging datasets from multiple locations.

The cleaned datasets were then combined into:

```text
data/punjab_rental_dataset.csv
```

---

## Feature Engineering

Feature Engineering was applied to extract additional information useful for rental price prediction.

### Original Features

* `bhk`
* `bathroom`
* `area`
* `location`
* `city`

### Engineered Features

#### Area Category

The property area is categorized into:

* Small
* Medium
* Large

Based on the project's defined area thresholds.

#### Furnishing

Furnishing information is extracted from property listing titles:

* Fully Furnished
* Semi Furnished
* Furnished
* Unknown

#### Property Type

Property types are extracted from listing titles:

* Apartment
* Flat
* Independent House
* Independent Floor
* Room Set
* PG
* Unknown

These features are integrated into the preprocessing pipeline before model training.

---

## Machine Learning Workflow

The project follows the following workflow:

```text
Raw OLX Data
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
One-Hot Encoding
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
Rent Prediction
```

---

## Models Implemented

The project currently contains **10 trained model configurations** across multiple regression algorithms.

### Traditional Regression Models

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Tuned Random Forest Regressor

### Boosting Models

* Gradient Boosting Regressor
* Tuned Gradient Boosting Regressor
* XGBoost
* Tuned XGBoost
* LightGBM
* Tuned LightGBM

Hyperparameter tuning was performed using **GridSearchCV** for selected models.

---

## Model Comparison

The models were evaluated using the same test set and compared using MAE, MSE, RMSE and R².

| Rank | Model                   |         MAE |        RMSE |         R² |
| ---: | ----------------------- | ----------: | ----------: | ---------: |
|    1 | **Random Forest Tuned** | **2409.65** | **3925.13** | **0.9156** |
|    2 | Random Forest           |     2415.63 |     3968.82 |     0.9137 |
|    3 | XGBoost                 |     4294.77 |     5965.17 |     0.8051 |
|    4 | LightGBM Tuned          |     4089.56 |     5966.82 |     0.8050 |
|    5 | Gradient Boosting Tuned |     4723.17 |     6477.87 |     0.7702 |
|    6 | XGBoost Tuned           |     4787.48 |     6643.71 |     0.7582 |
|    7 | LightGBM                |     4738.98 |     6936.62 |     0.7365 |
|    8 | Linear Regression       |     5235.75 |     7645.27 |     0.6799 |
|    9 | Gradient Boosting       |     5579.91 |     7880.15 |     0.6599 |
|   10 | Decision Tree           |     6253.57 |     8946.48 |     0.5616 |

> **Note:** The values above are from the project's current `outputs/metrics/model_comparison.csv`.

---

## Best Model

The current best-performing model is:

## Tuned Random Forest Regressor

### Performance

| Metric       |             Value |
| ------------ | ----------------: |
| **MAE**      |     **₹2,409.65** |
| **MSE**      | **15,406,626.23** |
| **RMSE**     |     **₹3,925.13** |
| **R² Score** |        **0.9156** |

An R² score of **0.9156** means the model explains approximately **91.56% of the variance** in rental prices on the evaluated test set.

The trained model is saved as:

```text
models/random_forest_tuned.pkl
```

---

## Evaluation Metrics

The models are evaluated using four standard regression metrics:

### MAE — Mean Absolute Error

Measures the average absolute difference between actual and predicted rent.

Lower is better.

### MSE — Mean Squared Error

Penalizes larger prediction errors more heavily.

Lower is better.

### RMSE — Root Mean Squared Error

Represents prediction error in the same unit as the target variable (₹).

Lower is better.

### R² — R-Squared

Measures how much variance in rental prices is explained by the model.

Higher is better.

---

## Prediction System

A reusable command-line prediction system has been implemented in:

```text
ml/predict.py
```

The system:

1. Loads the trained Random Forest model.
2. Loads the fitted preprocessing pipeline.
3. Accepts property details from the user.
4. Generates required engineered features.
5. Applies the same preprocessing used during training.
6. Generates the predicted monthly rent.

### Example Input

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

### Example Output

```text
========== Prediction ==========

Estimated Monthly Rent: ₹20,557.97
```

The prediction system also validates numerical inputs and uses predefined choices for categorical features to keep prediction inputs consistent with the training data.

---

## Model Analysis & Explainability

The repository also contains analysis tools for understanding model behaviour, including:

* Feature Importance
* Grouped Feature Importance
* Ablation Study
* Cross Validation
* SHAP Analysis

Generated analysis outputs include:

```text
outputs/figures/
├── ablation_study.png
├── feature_importance.png
├── shap_bar.png
├── shap_summary.png
└── shap_waterfall.png
```

These analyses help understand which features contribute to rental price predictions and how the model behaves.

---

## Power BI Dashboard

Before the Machine Learning phase, the rental data was also analyzed using **Power BI**.

The dashboard was used to explore:

* Rental price patterns
* BHK distribution
* Location-wise rental prices
* Property trends
* Dataset-level business insights

This helped establish an understanding of the dataset before moving into Machine Learning.

---

## Project Structure

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
├── insights.md
├── notes.md
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Tech Stack

### Programming & Data

* Python
* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* XGBoost
* LightGBM
* Joblib

### Visualization & Analysis

* Matplotlib
* Seaborn
* SHAP

### Business Intelligence

* Power BI

### Development

* Git
* GitHub

---

# Running the Prediction System

Clone the repository and install the required dependencies.

Then run:

```bash
py -m ml.predict
```

The program will ask for property details and return an estimated monthly rental price.

---

#  Current Status

##  Completed

* [x] Data Collection
* [x] Data Cleaning
* [x] Dataset Merging
* [x] Exploratory Data Analysis
* [x] Business Insights
* [x] Power BI Dashboard
* [x] Machine Learning Preprocessing
* [x] Feature Engineering
* [x] Linear Regression
* [x] Decision Tree
* [x] Random Forest
* [x] Random Forest Hyperparameter Tuning
* [x] Gradient Boosting
* [x] Gradient Boosting Tuning
* [x] XGBoost
* [x] XGBoost Tuning
* [x] LightGBM
* [x] LightGBM Tuning
* [x] Model Evaluation
* [x] Cross Validation
* [x] Model Comparison
* [x] Feature Importance Analysis
* [x] Ablation Study
* [x] SHAP Explainability
* [x] Prediction Pipeline
* [x] Validated User Input

---

## Next Phase

The Machine Learning experimentation and prediction pipeline are currently complete.

The next major phase is to build a **web application** around the trained model.

The planned application will provide a convenient user interface where users can enter property details and receive an estimated rental price without using the command line.

The exact UI, features and application architecture will be designed in the next phase.

Possible future extensions after the web application include:

* Model deployment
* Cloud hosting
* Additional data collection
* Model retraining with newer rental listings
* Further experimentation with additional algorithms such as CatBoost

---

## Author

**Harshpreet Singh**

A Computer Science student learning Machine Learning from scratch by building practical, real-world projects using Python and modern data science tools.

This project focuses on understanding **why each Machine Learning step is performed**, while maintaining a clean and modular project structure.

---

## ⭐ Project Goal

> **Turn real-world Punjab rental data into a practical rental price prediction system.**

The project started as a learning exercise in Data Analysis and Machine Learning and is now progressing toward a complete user-facing application.
