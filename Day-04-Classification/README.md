# Day 4 - Classification

Today I learned the basics of classification and practised it with a small Loan Approval dataset.

## What I learned

* Classification
* X and Y
* Train Test Split
* Logistic Regression
* KNN
* Decision Tree
* Random Forest
* Accuracy
* Prediction

## Dataset

I used these columns:

```text
Age
Income
LoanAmount
CreditScore
Experience
Approved
```

I used:

```text
X = Age, Income, LoanAmount, CreditScore, Experience

Y = Approved
```

The goal is to predict whether a loan will be approved or not.

## Models I used

### 1. Logistic Regression

Used Logistic Regression to predict the loan approval.

### 2. KNN

Used K-Nearest Neighbours for classification.

### 3. Decision Tree

Used a Decision Tree to make the prediction based on conditions.

### 4. Random Forest

Used Random Forest with multiple decision trees.

## Workflow

```text
Dataset
   ↓
X / Y
   ↓
Train Test Split
   ↓
Train Models
   ↓
Predictions
   ↓
Accuracy
   ↓
Compare Models
```

## New Customer Prediction

I also tested the models with a new customer:

```text
Age = 30
Income = 50000
LoanAmount = 150000
CreditScore = 700
Experience = 5
```

## What I understood

The main difference from Day 3 is:

```text
Day 3
Regression
→ Predict a number

Day 4
Classification
→ Predict a category
```

For this project, the model predicts whether the loan is approved or not.

## Day 4 Status

Completed.

Next: Day 5 - Unsupervised Learning and Customer Segmentation.
