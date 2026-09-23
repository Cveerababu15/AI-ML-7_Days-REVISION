# Day 6 - NLP and Text Classification

## Spam Email Classifier

Today I learned the basic NLP workflow and built a simple Spam Email Classifier.

The project takes text messages and predicts whether they are:

* Spam
* Not Spam

## What I Learned

* Basic text cleaning
* TF-IDF
* Train/Test Split
* Naive Bayes
* Text Classification
* Accuracy
* Precision
* Recall
* F1-score
* New text prediction

## Project Flow

```text
Text
 ↓
Clean Text
 ↓
TF-IDF
 ↓
Train/Test Split
 ↓
Naive Bayes
 ↓
Prediction
 ↓
Evaluation
```

## Technologies

* Python
* Pandas
* Scikit-learn

## Model

I used:

```text
Multinomial Naive Bayes
```

TF-IDF was used to convert text into numerical features before training the model.

## Prediction

The model can classify new messages as:

```text
Spam
Not Spam
```

## Main Learning

Machine learning models cannot directly work with normal text, so the text needs to be converted into numerical features.

In this project, TF-IDF was used for this purpose.

## Day 6 Status

Completed.

Next: Day 7 - End-to-End Machine Learning Project.
