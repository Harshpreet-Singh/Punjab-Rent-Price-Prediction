# Punjab Rent Price Prediction

A Machine Learning project that predicts rental property prices using real-world rental listings from Punjab. The project follows a complete end-to-end Machine Learning workflow, from data collection and preprocessing to feature engineering, model training, hyperparameter tuning, evaluation, and prediction.

---

# Project Objective

The goal of this project is to learn Machine Learning from scratch while building a production-style, modular codebase.

Objectives include:

* Build an accurate rental price prediction model.
* Understand every step of the Machine Learning pipeline.
* Apply Feature Engineering to improve model performance.
* Compare multiple regression algorithms.
* Follow clean software engineering practices.
* Build an interview-ready and GitHub-worthy project.

---

# Dataset

The dataset contains rental property listings collected from OLX for three cities in Punjab:

* SAS Nagar
* Mohali
* Kharar

### Dataset Size

* **13,877** rental listings

### Target Variable

* `price`

### Features Used

Original Features:

* `bhk`
* `bathroom`
* `area`
* `location`
* `city`

Engineered Features:

* `area_category`
* `furnishing`
* `property_type`

---

# Machine Learning Workflow

The project follows a complete Machine Learning pipeline:

* Data Cleaning
* Feature Engineering
* Feature Selection
* Train-Test Split
* One-Hot Encoding
* Model Training
* Hyperparameter Tuning
* Model Evaluation
* Model Comparison
* Rent Prediction

---

# Models Implemented

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Tuned Random Forest (GridSearchCV)

---

# Best Model Performance

**Model:** Random Forest (Hyperparameter Tuned)

| Metric   |       Value |
| -------- | ----------: |
| MAE      | **2409.65** |
| RMSE     | **3925.13** |
| R² Score |  **0.9156** |

Feature Engineering improved the tuned Random Forest model from **R² = 0.8729** to **R² = 0.9156**.

---

# Feature Engineering

Additional features were extracted from the dataset to improve prediction performance:

* Area Category (Small / Medium / Large)
* Furnishing Status
* Property Type

These engineered features significantly improved the model's predictive accuracy.

---

# Evaluation Metrics

Models are evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

---

# Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Matplotlib
* Power BI

---

# Project Structure

```text
Punjab-Rent-Price-Prediction/

├── data/
├── data_cleaning/
├── ml/
├── models/
├── outputs/
│   ├── figures/
│   ├── metrics/
│   └── predictions/
│
├── README.md
├── insights.md
├── notes.md
├── requirements.txt
└── .gitignore
```

---

# Current Status

**Completed**

* Data Collection
* Data Cleaning
* Exploratory Data Analysis (EDA)
* Business Insights
* Power BI Dashboard
* Dataset Merging
* Machine Learning Preprocessing
* Linear Regression
* Decision Tree
* Random Forest
* Hyperparameter Tuning
* Feature Engineering
* Model Evaluation
* Model Comparison
* Prediction System

---

# Future Improvements

* Feature Importance Analysis
* XGBoost
* LightGBM
* CatBoost
* Model Explainability
* Streamlit Web Application
* Deployment

---

# Author

**Harshpreet Singh**

Learning Machine Learning from Scratch using Python, Pandas and Scikit-learn while following clean software engineering practices.
