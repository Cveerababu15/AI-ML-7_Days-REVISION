# Day 7 - End-to-End Machine Learning

## Used Car Price Prediction

For the final day of my AI/ML revision, I built a simple Used Car Price Prediction project.

The goal is to predict the price of a used car using different car-related features.

## Features Used

* Age
* KM Driven
* Engine CC
* Number of Owners
* Service Score

Target:

* Price

## Project Flow

```text
Load Data
   ↓
Understand Data
   ↓
Check Missing Values
   ↓
Check Duplicates
   ↓
Basic EDA
   ↓
Select Features and Target
   ↓
Train/Test Split
   ↓
Linear Regression
   ↓
Random Forest
   ↓
Evaluate Models
   ↓
Compare Results
   ↓
Predict New Car
```

## Models Used

### Linear Regression

Used as a simple regression model and baseline.

### Random Forest Regressor

Used as a second model to compare its predictions with Linear Regression.

## Evaluation Metrics

I used:

* MAE
* RMSE
* R²

These metrics helped me understand the prediction errors and model performance.

## New Car Prediction

The model was tested with a new car having:

```text
Age = 3
KM Driven = 25000
Engine CC = 1500
Owners = 1
Service Score = 9
```

Both trained models were used to predict its price.

## What I Learned

Through this project I revised the complete machine learning workflow:

```text
Problem
 ↓
Data
 ↓
EDA
 ↓
Features
 ↓
Training
 ↓
Prediction
 ↓
Evaluation
 ↓
Model Comparison
```

I also understood that a very small dataset is useful for learning the workflow, but it is not enough to make strong real-world conclusions about model performance.

## Day 7 Status

Completed.

This completes my 7-day AI/ML revision journey.
