# Day 5 - Unsupervised Learning

## Customer Segmentation using K-Means

Today I learned the basics of Unsupervised Learning and K-Means Clustering.

For this project, I used customer data containing:

* Age
* Annual Income
* Spending Score

The goal was to divide customers into different groups based on their characteristics.

## What I Learned

* What is Unsupervised Learning
* What is Clustering
* K-Means Clustering
* What is K
* What is a Centroid
* Why distance is used in K-Means
* Why StandardScaler is important
* How to create clusters
* How to analyse the created clusters

## Project Flow

```text
CSV Data
   ↓
Load using Pandas
   ↓
Check the data
   ↓
Select features
   ↓
StandardScaler
   ↓
K-Means
   ↓
Create clusters
   ↓
Analyse clusters
```

## Features Used

```text
Age
AnnualIncome
SpendingScore
```

The `Customer` column was not used because it is only an ID.

## Model

I used K-Means with 3 clusters.

```python
KMeans(n_clusters=3, random_state=42, n_init=10)
```

## Result

K-Means grouped the customers into different clusters based on their age, income and spending score.

I also calculated the average values of each cluster to understand the characteristics of the customer groups.

## Day 5 Status

Completed.

Next: Day 6 - NLP and Text Classification.
