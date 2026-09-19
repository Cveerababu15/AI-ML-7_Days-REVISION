# Day 3 — Regression and House Price Prediction

## Overview

Day 3 of my AI/ML revision journey focused on understanding regression and building a House Price Prediction model.

The main goal was to understand the complete workflow from loading a dataset to training models, making predictions and evaluating their performance.

I worked with two regression algorithms:

* Linear Regression
* Random Forest Regressor

---

## Topics Practised

* Regression
* Features and target
* `X` and `y`
* Train/Test Split
* Linear Regression
* Random Forest Regression
* Predictions
* MAE
* MSE
* RMSE
* R²
* Basic overfitting

---

# Project — House Price Prediction

## Objective

The goal of the project is to predict house prices using information about the house.

The features used are:

* Area
* Bedrooms
* Bathrooms
* LocationScore
* HouseAge

The target is:

* Price

---

# Dataset

The dataset contains house-related information.

```text
Area
Bedrooms
Bathrooms
LocationScore
HouseAge
Price
```

The first five columns are used as features and `Price` is the target.

---

# Machine Learning Workflow

```text
House Price CSV
       ↓
Pandas
       ↓
X / y
       ↓
Train/Test Split
       ↓
Linear Regression
       ↓
Prediction
       ↓
MAE / MSE / RMSE / R²
       ↓
Random Forest Regression
       ↓
Prediction
       ↓
MAE / MSE / RMSE / R²
       ↓
Model Comparison
```

---

# Why Is This a Regression Problem?

House price prediction is a regression problem because the target variable is a continuous numerical value.

The model predicts values such as:

```text
₹35,00,000
₹45,00,000
₹52,00,000
₹68,00,000
```

The output is a number rather than a category.

---

# 1. Load the Dataset

I used Pandas to load the CSV file.

```python
df = pd.read_csv("./house_prices.csv")
```

---

# 2. Select Features and Target

The features are:

```python
X = df[
    [
        "Area",
        "Bedrooms",
        "Bathrooms",
        "LocationScore",
        "HouseAge"
    ]
]
```

The target is:

```python
Y = df["Price"]
```

Here:

* `X` represents the input features.
* `Y` represents the value the model needs to predict.

---

# 3. Train/Test Split

The dataset was divided into training and testing data.

```python
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)
```

The purpose is to train the model using one part of the dataset and evaluate it using unseen data.

---

# 4. Linear Regression

A Linear Regression model was created and trained using the training data.

```python
linear_model = LinearRegression()

linear_model.fit(X_train, Y_train)
```

The model was then used to make predictions:

```python
linear_predictions = linear_model.predict(X_test)
```

---

# 5. Model Evaluation

The Linear Regression model was evaluated using:

* MAE
* MSE
* RMSE
* R²

### MAE

Mean Absolute Error measures the average absolute difference between actual and predicted values.

### MSE

Mean Squared Error squares the prediction errors before calculating their average.

### RMSE

Root Mean Squared Error is the square root of MSE.

### R²

R² measures how well the model explains the variation in the target.

---

# 6. Random Forest Regression

After Linear Regression, I implemented Random Forest Regression to compare another regression algorithm on the same dataset.

The Random Forest model was trained using the same training data:

```python
random_forest_model.fit(X_train, Y_train)
```

Predictions were generated using:

```python
random_forest_predictions = random_forest_model.predict(X_test)
```

The same evaluation metrics were then calculated:

* MAE
* MSE
* RMSE
* R²

---

# Model Comparison

The two models were compared using the same testing data and evaluation metrics.

| Model             |           MAE |           MSE |          RMSE |            R² |
| ----------------- | ------------: | ------------: | ------------: | ------------: |
| Linear Regression | Actual Result | Actual Result | Actual Result | Actual Result |
| Random Forest     | Actual Result | Actual Result | Actual Result | Actual Result |

The final comparison is based on the actual results produced by the models.

---

# Overfitting Basics

Overfitting occurs when a model learns the training data too closely and does not generalise well to unseen data.

A simple way to understand it:

```text
Training Data
     ↓
Model learns very closely
     ↓
Very good training performance
     ↓
Poorer testing performance
     ↓
Possible Overfitting
```

For this revision, I focused on understanding the concept rather than applying advanced overfitting techniques.

---

# What I Learned

Day 3 helped me understand the complete basic regression workflow:

```text
Data
 ↓
Features and Target
 ↓
Train/Test Split
 ↓
Model Training
 ↓
Prediction
 ↓
Evaluation
 ↓
Model Comparison
```

I also understood that different regression algorithms can be trained on the same dataset and compared using common evaluation metrics.

---

# Day 3 Status

Completed

### Completed

* Regression understanding
* X / y
* Train/Test Split
* Linear Regression
* Prediction
* MAE
* MSE
* RMSE
* R²
* Random Forest Regression
* Random Forest evaluation
* Model comparison
* Basic overfitting understanding

Next: Day 4 — Classification.
