# Rent Prediction Project 


* Supervised Learning is a type of Machine Learning where the model learns from data that already contains the correct answers (labels).

- unsupervised learning ?? -> 
1. remove the Price column...
2. No prices., No labels., No correct answers.
3. Now the computer has to discover patterns on its own

* Unsupervised Learning is a type of Machine Learning where the data has no labels, and the model tries to discover patterns or groups on its own.

| Supervised Learning      | Unsupervised Learning             |
| ------------------------ | --------------------------------- |
| Has labels               | No labels                         |
| Knows the correct answer | Finds patterns itself             |
| Used for prediction      | Used for grouping and exploration |
| Example: Predict rent    | Example: Group similar houses     |



# What is a model?
- A model is simply the learned relationship between the input features and the target.


* here in my project 
```text
(BHK, Bathroom, Area, Location, City)
                ↓
          Machine Learning
                ↓
            Trained Model
                ↓
           Predicted Price
```

## 2 important terms :
- features (Input)
- target (Output)


# What is a Label?
- A label is simply the answer we want the model to learn.
* House Details = Features
* Price = Label (Target)


# 2 Types of supervised learning :  
1. Regression       - Used when the output is a number.   (predict salary, temperature)
2. Classification   - Used when the output is a category. (spam or not, pass or fail)




`and here price can't be a column then model would be considered as cheating `


# Final Features Set (Version 1)
| Column   | Use?          | Reason                                              |
| -------- | ------------- | --------------------------------------------------- |
| bhk      | YES           | Important predictor                                 |
| bathroom | YES           | Useful numeric feature                              |
| area     | YES           | Strong predictor                                    |
| location | YES           | Strong categorical feature                          |
| city     | YES           | Useful categorical feature                          |
| title    | NO (for now)  | Free-text feature; keep it for a future improvement |

# Target -> Price

* A good feature should have some relationship with the target.
* This process of choosing useful columns is called Feature Selection.



* you can't give mohali, kharar, sas nagar to model to train, because model work on numerical operations 
so what we need to do is "One-Hot Encoding"

| Feature  | Type        | Encoding?  |
| -------- | ----------- | ---------- |
| bhk      | Numeric     | No         |
| bathroom | Numeric     | No         |
| area     | Numeric     | No         |
| city     | Categorical | Yes        |
| location | Categorical | Yes        |

-------------------------------------------------------------------
first we need to know train-test split
like we can't train the model for 100% of data, it will be pure memorizing of the data 
so we will train using 80% and test using 20% that how correctly it predicts 

Training ≈ 11,101 rows
Testing ≈ 2,776 rows

* that's why we will see : test_size=0.2


* also fixing randomness of data 
By writing: random_state=42
we're telling Python: "Use the same random split every time.
- It ensures that data shuffling and train-test splits happen the exact same way every time you run the code. This reproducibility allows you to reliably compare different models or debug errors.


## visually : 

```text
Entire Dataset
       │
       ▼
┌───────────────────┐
│ Train-Test Split  │
└───────────────────┘
       │
       ├──────────────► Train Set
       │                  │
       │                  ▼
       │              Train Model
       │
       └──────────────► Test Set
                          │
                          ▼
                   Evaluate Model
```

* kinda move to actual model training now 
Pandas → Data handling
Matplotlib → Visualization
Scikit-learn → Machine Learning


`preprocessing.py 's responsibilities`

split and finalize data for training 


Where are those learned weights stored?

Inside the trained model.
* That's why we later save it as:
       models/
           linear_regression.pkl

- That .pkl file contains the learned parameters.

You don't need to train every time; Just load the saved model.

` train_model.py 's responsibilities`
Load data
        ↓
Preprocess data
        ↓
Train Linear Regression
        ↓
Save trained model




# Training my first model : 

1. When we write:

- model.fit(X_train, y_train)

Scikit-learn starts looking for patterns.

It asks questions like:
1. How much does area affect rent?
2. Does BHK matter?
3. Does bathroom matter?
4. How important is location?

Then it calculates the best weights.
Those weights become your trained model.



till version 1 of train_model.py 
CURRENT PIPELINE: 
Dataset
      ↓
Preprocessing
      ↓
Train-Test Split
      ↓
Encoding
      ↓
Linear Regression
      ↓
Saved Model


ml ---|
      |- preprocessing.py → prepares data.
      |- train_model.py → trains and saves both the model and the preprocessor.
      |- evaluate_model.py → loads the saved model and evaluates it.
      |- predict.py → loads both saved files to make predictions.



`evaluate_model.py 's responsibilities`

Load Model
        ↓
Load Preprocessor
        ↓
Preprocess Data
        ↓
Predict
        ↓
Calculate

1. MAE (Lower is Better)
MSE
2. RMSE (Lower is Better)
3. R² Score (Higher is Better)

========== Evaluation ==========

MAE  : 5341.42<br>
MSE  : 61204859.80<br>
RMSE : 7823.35<br>
R²   : 0.6648<br>


<hr>
<hr>
<hr>
<hr>

# summary_ver2.md's progress below


## Decision Tree instead of linear regression

WHY DECISION TREE ? 

because it asks question not just give answer by seeing only 1 factor

----------------------- VISUAL -----------------------

                    Area > 1500?

                   /            \

                No              Yes

             Area >1000?     Luxury?

             /      \         /     \

         ₹12k     ₹20k     ₹40k   ₹28k

* Why is it often better?

Linear Regression says:
- Everything follows one equation.

Decision Tree says:
- Different situations follow different rules.

That's much closer to real estate.

### problem in decision tree ??
- Overfitting

Think of two students.
Student A:

Understands concepts.
Can solve new questions.

Student B:
Memorized last year's paper.
Scores well only if the same questions appear.

* Decision Trees can become Student B if we let them grow without limits.

| Linear Regression                   | Decision Tree                              |
| ----------------------------------- | ------------------------------------------ |
| Fits one equation                   | Learns many decision rules                 |
| Assumes mostly linear relationships | Handles non-linear relationships naturally |
| Simple and interpretable            | Can model complex patterns                 |
| Fast                                | Can become complex                         |
| Less prone to overfitting           | Can overfit if unrestricted                |


later in decision tree we will make changes, trying to make it better 
The algorithm doesn't change. The training code doesn't change. Only the configuration changes. -> That's called hyperparameter tuning.

========== Evaluation ==========

MAE  : 6320.19<br>
MSE  : 80929287.71<br>
RMSE : 8996.07<br>
R²   : 0.5567

---------------------------------------------------------------------------------------------------------------------------------------

# Why do we need random forest ?

Instead of building one tree... it builds many trees.
Instead of trusting one tree... we trust the forest.

That's why it's called 'Random Forest'.

- Real-Life Analogy

Imagine asking for medical advice.

* One doctor Could make a mistake.
* A panel of 100 experienced doctors is Much more reliable.

* Random Forest works in the same spirit.

"What's a great first model for tabular data?"

# Random Forest is one of the most common answers because it:
-      works well on structured datasets,
-      handles non-linear relationships,
-      usually requires little preprocessing,
-      often performs well without extensive tuning.


========== Evaluation ========== 

MAE  : 3049.13<br>
MSE  : 23483264.20<br>
RMSE : 4845.95<br>
R²   : 0.8714


# decision tree v/s random forest

| Decision Tree      | Random Forest                               |
| ------------------ | ------------------------------------------- |
| Faster to train    | Slower                                      |
| Easy to visualize  | Difficult to visualize individual decisions |
| Small model        | Larger model                                |
| Can overfit easily | Usually generalizes better                  |




| Model             | How it thinks                                |
| ----------------- | -------------------------------------------- |
| Linear Regression | Draw one best-fit line                       |
| Decision Tree     | Ask a sequence of yes/no questions           |
| Random Forest     | Combine predictions from many decision trees |



| Model             |       MAE ↓ |      RMSE ↓ |       R² ↑ | Rank |
| ----------------- | ----------: | ----------: | ---------: | :--: |
| Linear Regression |     5341.42 |     7823.35 |     0.6648 |  🥈  |
| Decision Tree     |     6320.19 |     8996.07 |     0.5567 |  🥉  |
| **Random Forest** | **3049.13** | **4845.95** | **0.8714** |  🥇  |

make a file compare_models.py as we will not compare manually each model trained with each different algorithm, so we will make this file that gives model_comparison.csv that compares side by side 
==================================================
Comparing Machine Learning Models
==================================================

Evaluating: Linear Regression

Loading trained model...

Loading preprocessed data...

Making predictions...

========== Evaluation ==========

Model: Linear Regression

MAE  : 5341.42<br>
MSE  : 61204859.80<br>
RMSE : 7823.35<br>
R²   : 0.6648

Metrics saved to: outputs\metrics\linear_regression_metrics.txt

Evaluating: Decision Tree
Loading trained model...
Loading preprocessed data...
Making predictions...

========== Evaluation ==========

Model: Decision Tree

MAE  : 6320.19<br>
MSE  : 80929287.71<br>
RMSE : 8996.07<br>
R²   : 0.5567

Metrics saved to: outputs\metrics\decision_tree_metrics.txt

Evaluating: Random Forest
Loading trained model...
Loading preprocessed data...
Making predictions...

========== Evaluation ==========

Model: Random Forest

MAE  : 3049.13<br>
MSE  : 23483264.20<br>
RMSE : 4845.95<br>
R²   : 0.8714

Metrics saved to: outputs\metrics\random_forest_metrics.txt

==================================================
Final Model Comparison
==================================================
```text
               Model          MAE           MSE         RMSE        R2
2      Random Forest  3049.126716  2.348326e+07  4845.953384  0.871376
0  Linear Regression  5341.424574  6.120486e+07  7823.353488  0.664765
1      Decision Tree  6320.185282  8.092929e+07  8996.070682  0.556729
```
Comparison saved to: outputs\metrics\model_comparison.csv




<hr>
<hr>

### Completed till now : 
| Stage          | What You Learned                        |
| -------------- | --------------------------------------- |
| Data Cleaning  | Cleaning and preparing real-world data  |
| EDA            | Understanding patterns in data          |
| Preprocessing  | Preparing data for ML                   |
| Model Training | Training different algorithms           |
| Evaluation     | Measuring model performance             |
| Comparison     | Selecting the best model systematically |

---------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------


moving to prediction part now 
then the question comes 

How does the model know what 'Phase 7' means?<br>
ANSWER - It doesn't.

The preprocessor knows.

transformation is applied here by:
- transformed_data = preprocessor.transform(input_data)

That's why saving preprocessor.pkl earlier was so important—it ensures the model sees new inputs in exactly the same format as the training data.


# FIRST PREDICTION USING RANDOM_FOREST MODEL + PREPROCESSOR 

==================================================
Punjab Rent Price Prediction
==================================================

========== Enter Property Details ==========

BHK: 3
Bathroom: 2
Area (sqft): 1500
Location: Phase 7
City: SAS Nagar

========== Prediction ==========
Predicted Rent: ₹24,396.75



## Phase 1    &nbsp; &nbsp; &nbsp; &nbsp;    ✔ Data Cleaning

## Phase 2    &nbsp; &nbsp; &nbsp; &nbsp;    ✔ Exploratory Data Analysis

## Phase 3    &nbsp; &nbsp; &nbsp; &nbsp;    ✔ Power BI Dashboard

## Phase 4    &nbsp; &nbsp; &nbsp; &nbsp;    ✔ Machine Learning

- Linear Regression
- Decision Tree
- Random Forest

## Phase 5        ✔ Evaluation
- MAE
- RMSE
- R²

## Phase 6        ✔ Compare Models

Found the best model: Random Forest

## Phase 7        ✔ Prediction System

You can now predict rent for new houses.

<hr>
<hr>
<hr>
<hr>

# summary_ver3.md's progress below



we will do most important topic in ML
* Hyperparameter Tuning <br>
Parameter v/s Hyperparameter

- *Parameter:* These are learned during training, the algorithm figures them out automatically.

- *Hyperparameter:* These are chosen before training, the algorithm does not learn them.You decide them.

Example for Random Forest:<br>
      Number of trees = 100<br>
      Maximum depth = 15<br>
      Minimum samples split = 4

## Common Hyperparameters
| Hyperparameter      | Meaning                                     |
| ------------------- | ------------------------------------------- |
| `n_estimators`      | Number of trees                             |
| `max_depth`         | Maximum depth of each tree                  |
| `min_samples_split` | Minimum samples required to split a node    |
| `min_samples_leaf`  | Minimum samples required at a leaf          |
| `max_features`      | Number of features considered at each split |
| `bootstrap`         | Whether to sample with replacement          |

The goal of tuning is to find the combination that gives the best performance on unseen data;

`increasing the number doesn't always improve the model`

### Key Takeaways
* Parameters are learned automatically from data during training.
* Hyperparameters are chosen before training and control how the model learns.
* Different hyperparameter values can produce very different models.
* Hyperparameter tuning is the process of searching for the best settings.

<hr>
<hr>

**What is the goal of any ML model?**
The goal is: **Learn the underlying pattern so it can make accurate predictions on new, unseen data**

For example, our model learned from 13,877 rental listings.

We don't care if it predicts those same listings perfectly.

We care whether it can correctly predict the rent of **a brand-new house** that it has never seen before.

That ability is called **Generalization**


<hr>
<hr>

## 2 Type of Errors
1. High Bias 
2. High Variance

```text
---------- HIGH BIAS ----------   | ---------- HIGH VARIANCE ---------- 
The model is too simple.      | The model is too complex.
It doesn't learn enough.          | It memorizes the training data.
It misses important patterns.     | It performs poorly on unseen data.
This is called Underfitting . | This is called Overfitting.

```

Remember our old made models using different algorithms 
* Linear Regression - Very simple.  (higher bias.)
* Decision Tree - Very flexible.    (higher variance)
* Random Forest - Reduced variance by keeping model flexible.

Quick Recap
- High Bias → Underfitting: The model is too simple and misses important patterns.
- High Variance → Overfitting: The model is too complex and memorizes the training data.
- Good ML models generalize well to unseen data.
- Hyperparameters help control the balance between bias and variance.


## How do we reliably measure whether a model truly generalizes well instead of getting lucky with one train-test split?
- Everything after this (GridSearchCV, RandomizedSearchCV, Hyperparameter Tuning) depends on **Cross Validation.**
<!-- 
The Problem with Train-Test Split

Imagine you have 100 students.

You randomly select:

80 for practice
20 for the final exam

Suppose the 20 students happen to be the easiest ones.

Your student scores 95%.

Amazing?

Maybe.

Or maybe the exam was just easy.

Now imagine another random split.

This time the 20 students are the hardest ones.

Your student scores 82%.

Did the student's knowledge suddenly decrease?

No.

Only the test set changed.

Exactly the same thing happens in Machine Learning.

Different train-test splits can produce different results.

Example

Suppose we train Random Forest five times.

Each time, we randomly split the dataset differently. -->

## k-Fold Cross Validation

The most common method is k-Fold Cross Validation.

Suppose we choose:

k = 5

We divide the dataset into 5 equal parts (folds).

Dataset
```text
┌────┬────┬────┬────┬────┐
│ F1 │ F2 │ F3 │ F4 │ F5 │
└────┴────┴────┴────┴────┘
```
Now we train 5 times.

- `Round 1`
```text 
Test - [F1]

Train - [F2][F3][F4][F5]
```

- `Round 2 `
```text 
Train - [F1]

Test - [F2]

Train - [F3][F4][F5]
```
- `Round 3`
```text
Train - [F1][F2]

Test - [F3]

Train - [F4][F5]
```
- `Round 4`
```text
Train - [F1][F2][F3]

Test - [F4]

Train - [F5]
```
- `Round 5`
```text
Train - [F1][F2][F3][F4]

Test - [F5]
```

Every row in the dataset:

becomes part of the training set multiple times.
becomes part of the test set exactly once.

Nothing is wasted.

then the average score is considered : 
- Suppost : (0.87 + 0.86 + 0.88 + 0.85 + 0.87) / 5 = 0.866

_Instead of trusting one score, we trust the average._


**What Does k Mean?**

k is simply the number of folds

### Does Cross Validation Train the Final Model?

* This is a common misconception.

**No.**

Cross Validation is used to **evaluate different models** or different hyperparameter combinations.

After deciding which settings are best, **we train one final model on the full training data using those settings**.

<hr>

- Where Does It Fit?

Our workflow will become:

```text
Preprocessing
      ↓
Choose Hyperparameters
      ↓
Cross Validation
      ↓
Average Score
      ↓
Best Hyperparameters
      ↓
Train Final Model
      ↓
Evaluate on Test Set
      ↓
Save Model
```
_Notice that Cross Validation happens before saving the final model._


# Cross Validation vs Train-Test Split

| Train-Test Split              | Cross Validation                      |
| ----------------------------- | ------------------------------------- |
| One evaluation                | Multiple evaluations                  |
| Faster                        | Slower                                |
| Can depend on one lucky split | More reliable                         |
| Good for quick experiments    | Better for model selection and tuning |

## Quick Recap
- A single train-test split may give a lucky or unlucky score.
- Cross Validation evaluates the model multiple times using different train/test partitions.
- In k-Fold Cross Validation, every sample is used for training multiple times and for testing exactly once.
- We usually use the average score across all folds.
- GridSearchCV and RandomizedSearchCV rely on Cross Validation to compare hyperparameter settings fairly.


# GridSearchCV

- It compares different hyperparameter combinations.

* Suppose we want to test: max_depth(10,20,30)
GridSearchCV will automatically do: Train Model (max_depth=10 then 20 then 30)
and then choose the best score

suppose : We only gave 5 values:

3 depth values
2 tree values

**But GridSearchCV generated 6 models.**

This is why it's called Grid Search.

It creates a grid of all possible combinations

## visual workflow 
```text
Hyperparameter Grid

↓

Combination 1

↓

5-Fold CV

↓

Score

↓

Combination 2

↓

5-Fold CV

↓

Score

↓

Combination 3

↓

5-Fold CV

↓

Score

↓

...

↓

Best Combination
```

#### Why Is It Reliable?

Remember Cross Validation?

- Instead of evaluating each combination once...

- GridSearchCV evaluates each combination multiple times.

So if we have:

6 combinations and 5-fold Cross Validation

Python actually trains: 6 × 5 = **30 models**

# Why Not Always Use GridSearchCV?

Suppose we try:

```text
5 values of n_estimators

×

5 values of max_depth

×

4 values of min_samples_split

×

4 values of min_samples_leaf
```
Total combinations:
```text
5 × 5 × 4 × 4 = 400
```
With 5-fold Cross Validation:

```text
400 × 5 = 2,000 model trainings
```
That's why **GridSearchCV** can become slow as the search space grows.

This is exactly why RandomizedSearchCV exists—we'll cover that after using GridSearchCV.

### Quick Recap
GridSearchCV tests every possible hyperparameter combination.

- Each combination is evaluated using Cross Validation.
- It reports:
* `best_params_`
* `best_score_`
* `best_estimator_`
- It's thorough but can become computationally expensive with many hyperparameters and values.


# After using GridSearchCV

Grid Search Completed!

Best Parameters: {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 200}

**Best Cross Validation R²: 0.8031**

Earlier, _0.8714 was the test-set R²._

Now, _**0.8031** is the average Cross Validation R² over **5 folds**._

These are not the same thing, so `don't compare them directly.`

```text
| Earlier              | Now                                |
| -------------------- | ---------------------------------- |
| Test Set R²          | Cross Validation R²                |
| One train-test split | Average of 5 different splits      |
| Final evaluation     | Used for selecting hyperparameters |
```

### Final output of tune_random_forest.py
Best Parameters:
{'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 200}

Best Cross Validation R²: 0.8031

Metrics saved to: E:\Punjab-Rent-Price-Prediction\outputs\metrics\random_forest_tuned_metrics.txt

Model saved to: E:\Punjab-Rent-Price-Prediction\models\random_forest_tuned.pkl

========== Tuned Model Performance ==========
Model : Random Forest Tuned
MAE   : 2409.65
MSE   : 15406626.23
RMSE  : 3925.13
R²    : 0.9156


# comparing 4 models now (including random_forest_tuned.pkl)

==================================================
Comparing Machine Learning Models
==================================================

Evaluating: Linear Regression

Evaluating: Decision Tree

Evaluating: Random Forest

Evaluating: Random Forest Tuned

==================================================
Final Model Comparison
==================================================
                 Model          MAE           MSE         RMSE        R2
3  Random Forest Tuned  3040.463118  2.320717e+07  4817.382313  0.872888
2        Random Forest  3049.126716  2.348326e+07  4845.953384  0.871376
0    Linear Regression  5341.424574  6.120486e+07  7823.353488  0.664765
1        Decision Tree  6320.185282  8.092929e+07  8996.070682  0.556729


# SECOND PREDICTION USING RANDOM_FOREST_TUNED MODEL + PREPROCESSOR (preprocessor toh jruri hai side by side hona)
==================================================
Punjab Rent Price Prediction
==================================================

========== Enter Property Details ==========

BHK: 3
Bathroom: 2
Area (sqft): 1500
Location: Phase 7
City: SAS Nagar

========== Prediction ==========
Predicted Rent: ₹24,231.23



<hr>
<hr>
<hr>
<hr>

# summary_ver4.md's progress below



# FEATURE ENGINEERING
Feature Engineering means:

- Creating better input features from the existing data so that the model can learn patterns more easily.

## we will categorise the houses based on their area (small, medium, large)

using the ml/inspect.py file : output:

==================================================
Area Statistics
==================================================
count    13877.000000
mean      1260.748865
std        900.747353
min          1.000000
25%        750.000000
50%       1200.000000
75%       1680.000000
max      10000.000000
Name: area, dtype: float64

Quartiles:
0.25     750.0
0.50    1200.0
0.75    1680.0
Name: area, dtype: float64

| Condition  | Category |
| ---------- | -------- |
| <= 750     | Small    |
| 750 - 1680 | Medium   |
| > 1680     | Large    |


## we will work on the title and categorise on the basis of furnishing

| Title                | Feature         |
| -------------------- | --------------- |
| Fully Furnished 2BHK | Fully Furnished |
| semi-furnished flat  | Semi Furnished  |
| nothing mentioned    | Unknown         |


# after feature engineering there is a good shift 

```text
| Metric   | Before Feature Engineering | After Feature Engineering | Improvement |
| -------- | -------------------------: | ------------------------: | ----------: |
| **MAE**  |                    3040.46 |               **2409.65** |   ✅ -630.81 |
| **RMSE** |                    4817.38 |               **3925.13** |   ✅ -892.25 |
| **R²**   |                     0.8729 |                **0.9156** |   ✅ +0.0427 |
```

<hr>
<hr>
<hr>
<hr>

# summary_ver5.md's progress below


### feature importance file run krne se pta chlega which feature is more important - list of 20 is printed : 

```text
Top 20 Important Features
                                               Feature  Importance
527                                     remainder__bhk    0.327484
529                                    remainder__area    0.173760
528                                remainder__bathroom    0.110615
519                    categorical__furnishing_Unknown    0.016794
522       categorical__property_type_Independent Floor    0.011224
445            categorical__location_Sector 82, Mohali    0.011037
516            categorical__furnishing_Fully Furnished    0.009551
526                 categorical__property_type_Unknown    0.009429
447            categorical__location_Sector 85, Mohali    0.007887
461            categorical__location_Sector 98, Mohali    0.007722
325       categorical__location_Sector 21D, Chandigarh    0.006756
521                    categorical__property_type_Flat    0.006733
449            categorical__location_Sector 88, Mohali    0.006577
441            categorical__location_Sector 79, Mohali    0.006427
430           categorical__location_Sector 66B, Mohali    0.006237
518             categorical__furnishing_Semi Furnished    0.005750
420  categorical__location_Sector 60 Phase 3B2, Mohali    0.005692
428            categorical__location_Sector 66, Mohali    0.005515
517                  categorical__furnishing_Furnished    0.005332
429           categorical__location_Sector 66A, Mohali    0.005097
```

- after this feature_importance file was changed to correct/ remove the suffix used by preprocessor

Grouped Feature Importance
```text
Grouped Feature Importance

         Feature  Importance
2            BHK    0.327484
6       Location    0.302970
0           Area    0.173760
3       Bathroom    0.110615
7  Property Type    0.038707
5     Furnishing    0.037427
4           City    0.006256
1  Area Category    0.002780
```

# What is an Ablation Study?

The word ablation means removing something to measure its effect.


So far your project has answered:

- How accurate is the model? ✅
- Which features are important? ✅
- Did feature engineering help? ✅

Now we'll answer:

`Why did the model predict ₹X for this particular house?`

That's where **SHAP** comes in.


What is SHAP?

SHAP stands for:

**SHapley Additive exPlanations**

It comes from Shapley Values in game theory.

- The idea is simple:

Imagine 4 friends win ₹100.

How much money should each friend get?

Not equally.

The friend who contributed the most should receive more.

SHAP applies the same idea to machine learning.

Instead of friends, we have features.

### Why are we learning SHAP?

Because it's used in:

Google
Microsoft
Amazon
Kaggle competitions
Production ML systems

It's one of the most popular explainability tools today.

ml/shap_explain.py will :-
Load Model
        │
        ▼
Load Preprocessor
        │
        ▼
Preprocess Dataset
        │
        ▼
Create SHAP Explainer
        │
        ▼
Generate Summary Plot
        │
        ▼
Generate Bar Plot
        │
        ▼
Generate Waterfall Plot


# till summary_ver5.md 

<hr>
<hr>
<hr>
<hr>

# summary_ver6.md's progress below

1. ✅ Data Cleaning
2. ✅ Feature Engineering
3. ✅ Linear Regression
4. ✅ Decision Tree
5. ✅ Random Forest
6. ✅ Hyperparameter Tuning
7. ✅ Feature Importance
8. ✅ Ablation Study
9. ✅ SHAP Explainability
10. Cross Validation (final model robustness)
11. Model Error Analysis (find where predictions fail)
12. XGBoost / LightGBM / CatBoost comparison
13. Final model selection
14. Packaging / inference pipeline
15. Flask/FastAPI API
16. Streamlit Web App
17. Docker (optional)
18. Deployment
19. Documentation & README polish


# Cross Validation (Current Step)

Now the question has changed.

We're not asking:

`"Which parameters are best?"`

We're asking:

`"How reliable is my best model?"`

## think of an example: GridSearchCV

* Question: Who is the topper?
suppose **harsh is the topper**

* but cross validation checks 
if **harsh is performing best consistently ?**


# FINAL VERDICT 

```text
| Metric     | Result | Interpretation |
| ---------- | ------ | -------------- |
| Test R²    | ~0.916 | Excellent      |
| Mean CV R² | ~0.902 | Excellent      |
| Std Dev    | 0.0088 | Very Stable    |
```

* Conclusion : Your tuned Random Forest appears to generalize well on this dataset.

with saving output values of cross validation.py in outputs/metrics/cross_validation_metrics.txt

cross validation is completed

# Phase 1 (Model Validation) is officially complete.

```text
✅ Data Cleaning
✅ Feature Engineering
✅ Preprocessing Pipeline
✅ Linear Regression
✅ Decision Tree
✅ Random Forest
✅ Hyperparameter Tuning
✅ Feature Importance
✅ Ablation Study
✅ SHAP Explainability
✅ K-Fold Cross Validation

⬇️ NEXT LEVEL



🚀 Gradient Boosting
```

<hr>
<hr>
<hr>
<hr>

# summary_ver7.md's progress below

we'll start one of the biggest topics in classical ML:

```text
Gradient Boosting
        │
        ├── Gradient Boosting Regressor
        ├── XGBoost
        ├── LightGBM
        └── CatBoost
```


- Why Random Forest Isn't the Final Answer ?

✅ Less overfitting

✅ Better accuracy

✅ More stable predictions

✅ Handles nonlinear relationships

but - `It Doesn't Learn From Its Mistakes`

Every tree works independently.

But in gradient boosting 

example -
```text
student 1 solves paper 
 |
student 2 solves only the mistakes
 |
student 3 focuses on remaining
 |
next student fixes whats left 
```

```text
| Random Forest (Bagging)           | Boosting                           |
| --------------------------------- | ---------------------------------- |
| Trees are independent             | Trees depend on previous trees     |
| Built in parallel                 | Built sequentially                 |
| Averaging reduces variance        | Sequential correction reduces bias |
| Doesn't correct previous mistakes | Continuously corrects mistakes     |
| Faster to train                   | Usually slower to train            |
| Very robust                       | Often achieves higher accuracy     |
```

* Gradient Boosting does something similar—it takes small, sequential steps that reduce the prediction error at each stage.


## process in gradient boosting that helps it to make better decisions

```text
Tree 1
↓
Initial Prediction
↓
Residuals
↓
Tree 2
↓
Better Prediction
↓
New Residuals
↓
Tree 3
↓
Better Prediction
↓
Tree 4
↓
...
↓
Final Prediction
```

Why not build one huge, powerful tree?

Because a large tree can memorize the training data and overfit.

and improvements are done in small steps and gradually so it is "gradient" boosting <br/>
imagine adjusting the temp of AC in a room, we adjust it by 1 or 2°C not direct 10°C

comparison below -:

```text
| High Learning Rate         | Low Learning Rate               |
| -------------------------- | ------------------------------- |
| Learns quickly             | Learns slowly                   |
| Needs fewer trees          | Needs more trees                |
| Higher risk of overfitting | Usually better generalization   |
| Can miss the best solution | Often reaches a better solution |
```

## Gradient Boosting vs XGBoost vs LightGBM vs CatBoost

Many beginners think these are different algorithms.

They are not.

Think of them like this:

```text
Gradient Boosting
        │
        ├── XGBoost
        ├── LightGBM
        └── CatBoost
```
Gradient Boosting is the basic idea.

The other three are improved implementations of that idea.

```text
| Algorithm         | Best For                  | Speed     | Learning Difficulty |
| ----------------- | ------------------------- | --------- | ------------------- |
| Gradient Boosting | Learning concepts         | Medium    | ⭐ Very Easy        |
| XGBoost           | High accuracy             | Fast      | ⭐⭐               |
| LightGBM          | Huge datasets             | Very Fast | ⭐⭐⭐             |
| CatBoost          | Many categorical features | Fast      | ⭐⭐               |
```

### Which One Is Used Most?

- There isn't a single winner.

A common pattern is:

* Gradient Boosting → Learn the fundamentals.
* XGBoost → Strong all-round performer.
* LightGBM → Large datasets where speed matters.
* CatBoost → Datasets with many categorical features.


newer algorithm doesn't mean better performance <br>
gradient boosting is performing worse than random forest 

```text
Gradient Boosting Evaluation
========================================

MAE  : 5579.91
MSE  : 62096778.91
RMSE : 7880.15
R�   : 0.6599
```

### tuned the gradient_bosting model
========== Tuned Model Performance ==========
Model : Gradient Boosting Tuned
MAE   : 4723.17
MSE   : 41962852.17
RMSE  : 6477.87
R²    : 0.7702

## Why did XGBoost need to be created?

The answer is that traditional Gradient Boosting had several practical limitations:

- It was relatively slow on large datasets because trees were built sequentially without many implementation optimizations.
- It could overfit more easily without strong built-in regularization.
- It didn't make efficient use of hardware, so training could be much slower than necessary.
- Handling missing values and sparse data wasn't as robust as practitioners wanted.

Think of it like this:

* Gradient Boosting is a well-built family car.
* XGBoost is a race-tuned version of that car.

Xgboost Evaluation
========================================

MAE  : 4294.77

MSE  : 35583276.00

RMSE : 5965.17

R²   : 0.8051


# Current Leaderboard
```text
| Model                         |    MAE ↓ |   RMSE ↓ |      R² ↑ |
| ----------------------------- | -------: | -------: | --------: |
| Decision Tree                 |    ~6320 |    ~8996 |    ~0.557 |
| Linear Regression             |    ~5341 |    ~7823 |    ~0.665 |
| Gradient Boosting             |     5579 |     7880 |     0.660 |
| **Gradient Boosting (Tuned)** | **4723** | **6478** | **0.770** |
| **XGBoost (Default)**         | **4295** | **5965** | **0.805** |
| **Random Forest (Tuned)**     | **2409** | **3925** | **0.916** |

```

## After tuning xgboost it got even worse, but no matter we practised


```text
| Model                   |           R² |
| ----------------------- | -----------: |
| Decision Tree           |        0.557 |
| Gradient Boosting       |        0.660 |
| Linear Regression       |        0.665 |
| Gradient Boosting Tuned |        0.770 |
| XGBoost                 |    **0.805** |
| XGBoost Tuned           |        0.758 |
| Random Forest Tuned     | **0.916**    |
```

### we didn't use some more params in gridsearchcv that xgboost 

`they are part of advanced XGBoost optimization.`

gamma
min_child_weight
reg_alpha
reg_lambda
max_delta_step
grow_policy
tree_method
...


# Comparing all my boosting models

```text
========== Boosting Model Comparison ==========

                     Model      MAE  ...     RMSE      R2
0      Random Forest Tuned  2409.65  ...  3925.13  0.9156
1            Random Forest  2415.63  ...  3968.82  0.9137
2                  Xgboost  4294.77  ...  5965.17  0.8051
3  Gradient Boosting Tuned  4723.17  ...  6477.87  0.7702
4            Xgboost Tuned  4787.48  ...  6643.71  0.7582
5        Gradient Boosting  5579.91  ...  7880.15  0.6599
```

### Gradient Boosting had one weakness...

- It grows trees level by level.

Imagine this tree:

```text

          Root
         /    \
       A        B
      / \      / \
```

Gradient Boosting first grows the entire level.

### LightGBM thinks differently.

Instead of growing every branch equally, it asks:

- "Which leaf will reduce the error the most?"

Then it grows only that leaf.

Example:
```text
          Root
         /    \
       A        B
      /
     C
    /
   D
```

This is called **leaf-wise growth.**

<hr>
<hr>
<hr>
<hr>

# summary_ver8.md's progress below

=== LightGBM Results ===
Model: Lightgbm
MAE  : 4738.98
MSE  : 48116743.71
RMSE : 6936.62
R²   : 0.7365

```text
| Model                   |         MAE |        RMSE |         R² |
| ----------------------- | ----------: | ----------: | ---------: |
| Tuned Random Forest     | **2409.65** | **3925.13** | **0.9156** |
| Random Forest           | **2415.63** | **3968.82** | **0.9137** |
| XGBoost                 |     4294.77 |     5965.17 |     0.8051 |
| Gradient Boosting Tuned |     4723.17 |     6477.87 |     0.7702 |
| **LightGBM**            | **4738.98** | **6936.62** | **0.7365** |
| XGBoost Tuned           |     4787.48 |     6643.71 |     0.7582 |
| Gradient Boosting       |     5579.91 |     7880.15 |     0.6599 |
```

## After tuning lightgbm it turned somehow better 
Best Parameters:
{'learning_rate': 0.1, 'max_depth': -1, 'min_child_samples': 20, 'n_estimators': 300, 'num_leaves': 70}

Best Cross Validation R²: 0.7627

Evaluating tuned model...
Saving tuned model...
Saving metrics...

Metrics saved to: E:\Punjab-Rent-Price-Prediction\outputs\metrics\lightgbm_tuned_metrics.txt

=== Tuned LightGBM Results ===
Model: Lightgbm Tuned
MAE  : 4089.56
MSE  : 35602914.83
RMSE : 5966.82
R²   : 0.8050

```text
| Model                   |           R² |
| ----------------------- | -----------: |
| Random Forest Tuned     | **0.9156** ⭐ |
| Random Forest           |   **0.9137** |
| XGBoost                 |   **0.8051** |
| LightGBM Tuned          |   **0.8050** |
| XGBoost Tuned           |   **0.7582** |
| Gradient Boosting Tuned |   **0.7702** |
| LightGBM                |   **0.7365** |
```


==================================================
Final Model Comparison <br>
==================================================

```text
                     Model      MAE          MSE     RMSE      R2
3      Random Forest Tuned  2409.65  15406626.23  3925.13  0.9156
2            Random Forest  2415.63  15751541.04  3968.82  0.9137
6                  Xgboost  4294.77  35583276.00  5965.17  0.8051
9           Lightgbm Tuned  4089.56  35602914.83  5966.82  0.8050
5  Gradient Boosting Tuned  4723.17  41962852.17  6477.87  0.7702
7            Xgboost Tuned  4787.48  44138880.00  6643.71  0.7582
8                 Lightgbm  4738.98  48116743.71  6936.62  0.7365
0        Linear Regression  5235.75  58450174.08  7645.27  0.6799
4        Gradient Boosting  5579.91  62096778.91  7880.15  0.6599
1            Decision Tree  6253.57  80039427.03  8946.48  0.5616
```


### Comparing models 

```text
| Rank | Model                   |         R² | Verdict             |
| ---- | ----------------------- | ---------: | ------------------- |
| 🥇   | Random Forest Tuned     | **0.9156** | Best model          |
| 🥈   | Random Forest           | **0.9137** | Almost identical    |
| 🥉   | XGBoost                 | **0.8051** | Good                |
| 4    | LightGBM Tuned          | **0.8050** | Good                |
| 5    | Gradient Boosting Tuned | **0.7702** | Average             |
| 6    | XGBoost Tuned           | **0.7582** | Worse than baseline |
| 7    | LightGBM                | **0.7365** | Baseline            |
| 8    | Linear Regression       | **0.6799** | Good baseline       |
| 9    | Gradient Boosting       | **0.6599** | Weak                |
| 10   | Decision Tree           | **0.5616** | Weak                |
```


PS E:\Punjab-Rent-Price-Prediction> py -m ml.predict
==================================================
Punjab Rent Price Prediction
==================================================

========== Enter Property Details ==========

BHK: 3
Bathroom: 2
Area (sqft): 1500
Location: Phase 7
City: SAS Nagar
Furnishing (Fully Furnished / Semi Furnished / Furnished / Unknown): Semi Furnished
Property Type (Apartment / Flat / Independent House / Independent Floor / Room Set / PG / Unknown): Flat

========== Prediction ==========
Estimated Monthly Rent: ₹20,557.97



# Giving UI to my project

```text
             KIRA
              │
       React Frontend
              │
          HTTP POST
              │
              ▼
       ┌──────────────┐
       │   FastAPI    │
       │   Backend    │
       └──────┬───────┘
              │
       Load ML artifacts
              │
       ┌──────┴───────┐
       │              │
 preprocessor.pkl  RF model
       │              │
       └──────┬───────┘
              │
        predicted rent
              │
              ▼
        JSON response
              │
              ▼
       React Result UI
```



## load frontend : `npm run dev` in E:\Punjab-Rent-Price-Prediction\kira\frontend>

## load backend : `.\.venv\Scripts\Activate.ps1` in E:\Punjab-Rent-Price-Prediction\kira\backend>
##  then run `uvicorn main:app --reload`



### in main.py in ./backend

we are adding pydantic validation 

bhk: int = Field(..., ge=1, le=10)

So FastAPI automatically rejects:
```
{
  "bhk": -2
}
```
instead of sending nonsense into your model.

similarly for area and for furnishing etc too

### CORS limitation too 

allow_origins only from 5173 port of localhost

Without CORS, the browser can block your React request.

for being safe side also gave main.py try exception, error handling


# NOW THE ML PIPELINE IS :

```
Request
   ↓
Pydantic validation
   ↓
Feature engineering
   ↓
Preprocessor
   ↓
Random Forest Tuned
   ↓
₹17,922.67
```

```

1. Project Idea

Punjab Rent Price Prediction using real rental listing data.

2. Data Collection

Collected rental listings from OLX for Punjab locations.

3. Raw Dataset Preparation

Combined the scraped datasets from SAS Nagar, Mohali and Kharar.

4. Data Cleaning

Removed irrelevant columns, invalid listings, duplicates, sale listings and problematic values.

5. Property Feature Extraction

Extracted BHK, bathroom, area and other useful property information.

6. Dataset Consolidation

Created the final punjab_rental_dataset.csv with around 13,877 listings.

7. Exploratory Data Analysis

Inspected distributions, missing values, property sizes, BHK counts and rental patterns.

8. ML Preprocessing

Built the reusable preprocessing pipeline with ColumnTransformer and OneHotEncoder.

9. Feature Engineering

Added area_category, furnishing and property_type.

10. Linear Regression

Trained and evaluated the baseline Linear Regression model.

11. Decision Tree

Trained and evaluated the Decision Tree model.

12. Random Forest

Trained Random Forest and significantly improved prediction performance.

13. Random Forest Tuning

Tuned Random Forest and selected random_forest_tuned.pkl as the main model.

14. Gradient Boosting

Trained and evaluated Gradient Boosting.

15. XGBoost

Trained and evaluated XGBoost and its tuned version.

16. Model Comparison

Compared Random Forest, tuned Random Forest, Gradient Boosting and XGBoost.

17. Final Model Selection

Selected Tuned Random Forest as the primary production prediction model.

18. Prediction Script

Created reusable Python prediction logic using the saved model and preprocessor.

19. KIRA Concept

Started building KIRA as the user-facing rent intelligence application.

20. KIRA Frontend Setup

Created React + Vite frontend architecture.

21. Tailwind CSS

Integrated Tailwind CSS into the KIRA frontend.

22. KIRA Design System

Created the minimal premium visual direction with lock-violet branding.

23. KIRA Hero

Built the large typography-based hero section.

24. KIRA Navigation

Built the minimal navigation and interaction elements.

25. How KIRA Works

Created the three-step explanation section.

26. Rent Estimator UI

Created the property input form for rent prediction.

27. Location Selection

Designed city/location selection instead of manual location typing.

28. Prediction Result UI

Created the dedicated estimated-rent result section.

29. UI Animations

Added hover, transition, reveal and interaction effects.

30. 3D Experiment

Experimented with React Three Fiber and a GLB house model.

31. 3D Decision

Dropped the 3D implementation because it distracted from the actual ML/product goal.

32. KIRA UI v1

Completed and committed the first polished KIRA interface.

33. KIRA UI Enhancement

Added interaction and hover improvements.

34. FastAPI Backend

Created the KIRA backend using FastAPI.

35. ML Artifact Integration

Connected FastAPI to random_forest_tuned.pkl and preprocessor.pkl.

36. Prediction Endpoint

Created POST /predict.

37. API Validation

Added Pydantic validation for property inputs.

38. API Error Handling

Added proper prediction error handling.

39. CORS Configuration

Configured FastAPI to communicate with the React development server.

40. Backend Testing

Successfully tested a real prediction returning ₹17,922.67.

41. Validation Testing

Successfully confirmed invalid inputs return 422 validation errors.

What's Pending
42. React → FastAPI Integration

Connect RentForm.jsx to /predict.

43. Real Prediction Result

Replace the current ₹ — placeholder with the actual prediction.

44. Loading State

Show a polished loading state while the model predicts.

45. Prediction Error State

Handle backend/network errors gracefully in the UI.

46. Result Experience

Make the prediction result feel like a proper KIRA experience rather than plain JSON.

47. Rent Confidence / Estimate Context

Add something professional around the prediction, such as an estimated range or confidence indicator only if we can calculate it honestly from the model/data.

48. Form Validation

Add frontend validation before sending requests.

49. Location Data

Replace the temporary hard-coded locations with a cleaner structured location dataset based on the actual training data.

50. API Configuration

Move the backend URL into a frontend environment variable instead of hard-coding it.

51. Production Backend Structure

Cleanly separate API schemas, model loading, prediction logic and configuration if the project grows.

52. API Documentation

Improve the FastAPI documentation and endpoint descriptions.

53. Security / Production Hardening

Add appropriate production CORS, environment configuration and request safeguards.

54. Testing

Add backend tests for valid predictions, invalid inputs and edge cases.

55. Frontend Responsiveness

Polish mobile/tablet layouts.

56. Accessibility

Improve labels, keyboard navigation, focus states and semantic structure.

57. Performance Optimization

Optimize frontend assets and model-loading behavior.

58. Deployment

Deploy the KIRA frontend and FastAPI backend.

59. Production Model Packaging

Decide how the .pkl artifacts should be stored and loaded in deployment.

60. Production Environment

Configure environment variables, API URLs and deployment-specific settings.

61. Final Portfolio Polish

Add README, architecture diagram, screenshots, model metrics and project explanation.

62. GitHub Documentation

Document the complete ML → API → React pipeline.

63. Final KIRA Demo

Create the polished end-to-end portfolio demonstration.
```