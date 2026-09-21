import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load the data
df = pd.read_csv("./Data/customers.csv")

print("Data Loaded:")
print(df)

# Understand the data
print("\nFirst 5 rows:")
print(df.head())

print("\nData Information:")
print(df.info())

print("\nData Description:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Select features
X = df[["Age", "AnnualIncome", "SpendingScore"]]

# StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nScaled Data:")
print(X_scaled)

# K-Means
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

model.fit(X_scaled)

# Get the clusters
clusters = model.labels_

print("\nClusters:")
print(clusters)

# Add clusters to DataFrame
df["Cluster"] = clusters

print("\nCustomer Data with Clusters:")
print(df)

# Understand the clusters
print("\nAverage values for each Cluster:")
print(
    df.groupby("Cluster")[["Age", "AnnualIncome", "SpendingScore"]].mean()
)