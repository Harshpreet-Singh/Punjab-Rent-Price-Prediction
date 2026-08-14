# KIRA — Prediction Explanation & Feature Influence Notes

## Evaluation Question: What does "Influence" mean in KIRA?

### Question

**What does "Strong / Moderate / Small influence" mean in the prediction result?**

### Answer

The **Influence** shown by KIRA represents how sensitive the trained rental prediction model is to a particular feature for the **specific property being evaluated**.

KIRA currently uses a **local counterfactual comparison** to estimate this influence.

The process is:

1. KIRA calculates the original rent prediction.
2. One feature is changed while the other property details are kept constant.
3. KIRA runs the prediction again with this changed value.
4. The difference between the original and comparison predictions is treated as that feature's **local impact**.
5. The absolute size of this impact is converted into a UI label: **Strong**, **Moderate**, or **Small influence**.

---

## Example

Suppose KIRA predicts:

**Original prediction: ₹23,278**

For the bathroom feature, KIRA changes the property from 2 bathrooms to 1 bathroom while keeping the other property details unchanged.

Suppose the new prediction becomes:

**Counterfactual prediction: ₹20,535**

Then:

```text
Impact = Original prediction - Counterfactual prediction

       = ₹23,278 - ₹20,535

       = +₹2,743
```

KIRA can therefore display:

```text
Bathrooms
2
+₹2,743
Strong influence
```

This means that, for this particular property and comparison, the model's prediction changes by approximately ₹2,743 when the bathroom value is changed.

---

# Important: Influence Is Not Causation

The feature impact should **not** be interpreted as a guaranteed real-world rent increase or decrease.

For example, if KIRA displays:

```text
Bathrooms
+₹2,743
```

we should NOT say:

> "Having two bathrooms increases the actual market rent by ₹2,743."

The correct interpretation is:

> "For this particular property, the model's prediction changes by approximately ₹2,743 when the bathroom value is changed in the controlled comparison."

Therefore, KIRA's explanation describes **model sensitivity**, not a causal relationship in the real rental market.

---

# Positive and Negative Impact

## Positive Impact

A positive impact means that the current feature value produces a **higher model prediction than the chosen counterfactual value**.

Example:

```text
Bathrooms
+₹2,743
```

The prediction for the current bathroom value is approximately ₹2,743 higher than the prediction for the comparison value.

## Negative Impact

A negative impact means that the current feature value produces a **lower model prediction than the chosen counterfactual value**.

Example:

```text
Furnishing
-₹7,291
```

This does NOT mean:

> "Furnishing always decreases rent by ₹7,291."

It means that, under the specific counterfactual comparison used by KIRA, the model predicted approximately ₹7,291 less for the current value than for the comparison value.

---

# Influence Classification

KIRA converts the numerical impact into a simpler label for the UI.

| Absolute Impact | Influence Label |
|---:|---|
| ≥ ₹2,500 | Strong influence |
| ₹1,000 – ₹2,499 | Moderate influence |
| < ₹1,000 | Small influence |

These thresholds are **heuristic presentation thresholds**.

They are used to make raw numerical impacts easier for users to understand.

They are:

- not confidence intervals
- not probability scores
- not statistical significance levels
- not directly produced by the Random Forest model

The underlying model produces the prediction; KIRA's explanation layer calculates the local comparison and classifies its magnitude for presentation.

---

# Why Is Location Not Currently Shown as an Influence?

Location is an important feature in KIRA's prediction model.

However, it is currently not included in the feature-impact explanation because the dataset contains a very large number of unique locations — approximately **510 location categories** are represented in the trained OneHotEncoder.

A meaningful counterfactual for numerical features such as area or count-based features such as bathrooms is relatively straightforward.

For location, arbitrarily changing:

```text
Sector 70, Mohali
```

to another location could create an explanation that is difficult to interpret and may not represent a useful comparison.

Therefore, KIRA currently avoids presenting a potentially misleading location impact and focuses the explanation on features for which a controlled comparison can be defined more clearly.

---

# Current Features Explained by KIRA

The current explanation layer can provide local impacts for:

- Area
- Bedrooms
- Bathrooms
- Furnishing
- Property type

The results are sorted by **absolute impact**, so the features with the largest model sensitivity appear first.

Example:

```text
Bathrooms       +₹2,743   Strong influence
Area            +₹2,100   Moderate influence
Furnishing      -₹1,400   Moderate influence
Bedrooms        +₹900     Small influence
```

---

# Why Use Local Explanation?

KIRA is not only intended to return a rent number.

A prediction such as:

```text
₹23,278
```

does not tell the user why the model arrived at that estimate.

The feature-impact section provides additional transparency by showing how the model responds to controlled changes in individual property features.

This makes the prediction easier to interpret and gives the user more context around the estimate.

---

# Prediction vs Feature Influence

These are two different concepts.

### Prediction

The Random Forest model predicts the estimated monthly rent:

```text
Estimated monthly rent
₹23,278
```

### Feature Influence

The explanation layer asks:

> "How much does the model's prediction change when this particular feature is changed while the other details remain fixed?"

Example:

```text
Bathrooms
+₹2,743
```

The feature impact is **not another prediction**. It is a local sensitivity measurement derived from additional model predictions.

---

# Important Technical Limitation

The current approach is a **local counterfactual explanation**, not a full causal analysis.

The impact depends on:

- the specific property being evaluated
- the selected counterfactual value
- the trained Random Forest model
- the feature interactions learned by the model

Therefore, the same feature can have a different impact for different properties.

For example:

```text
Property A → Area impact: +₹3,000
Property B → Area impact: +₹800
```

This does not necessarily mean that the model is inconsistent.

It means the model can respond differently to the same feature depending on the other characteristics of the property.

---

# Best Viva / Evaluation Answer

### If asked: "How did you calculate feature influence?"

Use this answer:

> **"KIRA uses local counterfactual analysis. We change one property feature at a time while keeping the other property details constant, run the trained Random Forest model again, and calculate the difference between the original and counterfactual predictions. This difference represents the feature's local influence on the model's prediction. It explains model sensitivity for that particular property rather than claiming a causal relationship."**

### Short Version

> **"Influence tells us how much KIRA's prediction changes when one feature is changed while the rest of the property remains constant. It is a local model-sensitivity measure, not a causal claim."**

---

# Possible Evaluation Follow-up Questions

## Q1. Does +₹2,743 mean the feature increases actual market rent by ₹2,743?

**Answer:**

No.

It means the trained model's prediction changed by approximately ₹2,743 under the controlled comparison. It does not establish a causal relationship in the real rental market.

## Q2. Why can a feature have a negative impact?

**Answer:**

A negative impact means the current feature value produces a lower prediction than the chosen counterfactual value. It reflects the model's learned behavior for that specific property and comparison.

## Q3. Why are there Strong, Moderate and Small influence labels?

**Answer:**

The labels are a user-friendly classification of the numerical impact. KIRA currently uses heuristic thresholds based on the absolute impact:

```text
≥ ₹2,500      → Strong
₹1,000–2,499  → Moderate
< ₹1,000      → Small
```

They are presentation labels rather than statistical confidence measures.

## Q4. Why didn't you use Location in the explanation?

**Answer:**

Location is represented by hundreds of one-hot encoded categories in the model. Choosing an arbitrary alternative location would not necessarily create a meaningful counterfactual explanation, so the current version avoids presenting a potentially misleading location impact.

## Q5. Is this SHAP?

**Answer:**

No.

KIRA explored SHAP during development, but the current production explanation shown in the application uses **controlled counterfactual predictions**.

The current feature-impact values are therefore local sensitivity measurements based on repeated model predictions, rather than SHAP values.

## Q6. Does this explanation affect the prediction?

**Answer:**

No.

The prediction is generated by the trained Random Forest model.

The explanation layer runs additional predictions only to understand and communicate how the model responds to controlled feature changes. It does not modify the original prediction.

## Q7. Why is this useful to a user?

**Answer:**

A rent estimate alone gives the user a number but provides little context.

The feature-impact section gives the user an interpretable view of which supported property characteristics had the strongest influence on the model's estimate for their particular property.

---

# One-Line Technical Definition

> **KIRA's feature influence is a local counterfactual sensitivity measure calculated as the difference between the original model prediction and a prediction generated after changing one feature while keeping the remaining property details constant.**

---

# Important Terminology

| Term | Meaning |
|---|---|
| Random Forest | Trained regression model used by KIRA to predict rent |
| Prediction | Estimated monthly rent produced by the model |
| Counterfactual | A modified version of the same property used for comparison |
| Local explanation | Explanation specific to one particular input property |
| Feature impact | Difference between original and counterfactual predictions |
| Influence | User-friendly interpretation of the magnitude of feature impact |
| Strong / Moderate / Small | Heuristic UI categories based on absolute impact |
| Causation | NOT claimed by KIRA's current explanation method |
| SHAP | Explored during development, but not used for the current displayed explanation |

---

# Final Takeaway

KIRA's explanation system follows this flow:

```text
Property Input
      ↓
Original Random Forest Prediction
      ↓
Change ONE feature
      ↓
Counterfactual Prediction
      ↓
Calculate Prediction Difference
      ↓
Feature Impact
      ↓
Classify Impact
      ↓
Strong / Moderate / Small Influence
      ↓
Display to User
```

The key idea to remember for evaluation is:

> **KIRA explains how sensitive its trained model is to individual property features for a specific prediction. It does not claim that those features causally determine the real-world rental price.**
