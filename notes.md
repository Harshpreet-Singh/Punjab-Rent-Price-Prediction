# rent prediction project is a Supervised Regression problem.

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


# 2 types of supervised learning :  
1. Regression       - Used when the output is a number.   (predict salary, temperature)
2. Classification   - Used when the output is a category. (spam or not, pass or fail)


<!-- and here price can't be a column then model would be considered as cheating  -->

# Final Features Set (Version 1)
| Column   | Use?          | Reason                                              |
| -------- | ------------- | --------------------------------------------------- |
| bhk      | YES           | Important predictor                                 |
| bathroom | YES           | Useful numeric feature                              |
| area     | YES           | Strong predictor                                    |
| location | YES           | Strong categorical feature                          |
| city     | YES           | Useful categorical feature                          |
| title    | NO (for now)  | Free-text feature; keep it for a future improvement |

# target -> Price

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
we're telling Python: "Use the same random split every time."
- It ensures that data shuffling and train-test splits happen the exact same way every time you run the code. This reproducibility allows you to reliably compare different models or debug errors.


#### visually : 
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



* kinda move to actual model training now 
Pandas → Data handling
Matplotlib → Visualization
Scikit-learn → Machine Learning


<!-- preprocessing.py 's responsibilities  -->
split and finalize data for training 


Where are those learned weights stored?

Inside the trained model.
* That's why we later save it as:
       models/
           linear_regression.pkl

- That .pkl file contains the learned parameters.

You don't need to train every time; Just load the saved model.


<!-- train_model.py 's responsibilities -->
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



<!-- evaluate_model.py 's responsibilities -->
Load Model
        ↓
Load Preprocessor
        ↓
Preprocess Data
        ↓
Predict
        ↓
Calculate

MAE
MSE
RMSE
R²

========== Evaluation ==========
MAE  : 5341.42
MSE  : 61204859.80
RMSE : 7823.35
R²   : 0.6648



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

