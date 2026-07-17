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
