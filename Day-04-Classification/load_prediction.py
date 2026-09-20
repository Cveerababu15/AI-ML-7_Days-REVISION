import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv("./Data/load_data.csv")
print(df)


X = df[["Age", "Income", "LoanAmount", "CreditScore", "Experience"]]

Y = df["Approved"]
Y = Y.values.ravel()


# Train the data
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)


# Logistic Regression
model = LogisticRegression()
model.fit(X_train, Y_train)

predictions = model.predict(X_test)
print(predictions)


# Accuracy
accuracy = accuracy_score(Y_test, predictions)
print("\nAccuracy:", accuracy)


# KNN
knn_model = KNeighborsClassifier()
knn_model.fit(X_train, Y_train)

knn_prediction = knn_model.predict(X_test)

print("\nKNN Predictions:")
print(knn_prediction)

knn_accuracy = accuracy_score(
    Y_test,
    knn_prediction
)

print("KNN Accuracy:", knn_accuracy)


# Decision Tree
Decision_model = DecisionTreeClassifier(max_depth=2)
Decision_model.fit(X_train, Y_train)

Decision_prediction = Decision_model.predict(X_test)

print("\nDecision Tree Predictions:")
print(Decision_prediction)

Decision_Accuracy = accuracy_score(
    Y_test,
    Decision_prediction
)

print("Decision Tree Accuracy:", Decision_Accuracy)


# Random Forest
rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=4,
    random_state=42
)

rf_model.fit(X_train, Y_train)

rf_prediction = rf_model.predict(X_test)

print("\nRandom Forest Predictions:")
print(rf_prediction)

rf_accuracy = accuracy_score(
    Y_test,
    rf_prediction
)

print("Random Forest Accuracy:", rf_accuracy)


# New Customer
new_customer = pd.DataFrame(
    [[30, 50000, 150000, 700, 5]],
    columns=["Age", "Income", "LoanAmount", "CreditScore", "Experience"]
)


LogicR = model.predict(new_customer)
knn_prediction = knn_model.predict(new_customer)
Decision_prediction = Decision_model.predict(new_customer)
rf_prediction = rf_model.predict(new_customer)


print("\nNew Customer Prediction:")
print("Logistic Regression Model:", LogicR)
print("KNN Prediction Model:", knn_prediction)
print("Decision Tree Model:", Decision_prediction)
print("Random Forest Model:", rf_prediction)