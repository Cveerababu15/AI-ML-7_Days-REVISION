import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Load the data
df = pd.read_csv("./Data/car_price.csv")

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


# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())


# Basic EDA
print("\nAverage Price:", df["Price"].mean())
print("Highest Price:", df["Price"].max())
print("Lowest Price:", df["Price"].min())


# Price vs KM
print("\nPrice and KM Driven:")
print(df[["KM_Driven", "Price"]])


# Price vs Age
print("\nPrice and Age:")
print(df[["Age", "Price"]])


# Features and target
X = df[["Age", "KM_Driven", "EngineCC", "Owners", "ServiceScore"]]
y = df["Price"]


# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Linear Regression
linear_model = LinearRegression()

linear_model.fit(X_train, y_train)

linear_predictions = linear_model.predict(X_test)


# Linear Regression Evaluation
linear_mae = mean_absolute_error(y_test, linear_predictions)
linear_rmse = np.sqrt(
    mean_squared_error(y_test, linear_predictions)
)
linear_r2 = r2_score(y_test, linear_predictions)

print("\nLinear Regression Results:")
print("MAE:", linear_mae)
print("RMSE:", linear_rmse)
print("R2:", linear_r2)


# Random Forest
rf_model = RandomForestRegressor(
    n_estimators=100,
    max_depth=4,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)


# Random Forest Evaluation
rf_mae = mean_absolute_error(y_test, rf_predictions)
rf_rmse = np.sqrt(
    mean_squared_error(y_test, rf_predictions)
)
rf_r2 = r2_score(y_test, rf_predictions)

print("\nRandom Forest Results:")
print("MAE:", rf_mae)
print("RMSE:", rf_rmse)
print("R2:", rf_r2)


# Model Comparison
print("\nModel Comparison:")

print(
    "Linear Regression -",
    "MAE:", linear_mae,
    "RMSE:", linear_rmse,
    "R2:", linear_r2
)

print(
    "Random Forest -",
    "MAE:", rf_mae,
    "RMSE:", rf_rmse,
    "R2:", rf_r2
)


# New Car Prediction
new_car = pd.DataFrame(
    [[3, 25000, 1500, 1, 9]],
    columns=[
        "Age",
        "KM_Driven",
        "EngineCC",
        "Owners",
        "ServiceScore"
    ]
)

linear_price = linear_model.predict(new_car)
rf_price = rf_model.predict(new_car)

print("\nNew Car Prediction:")

print("Linear Regression Price:", linear_price[0])
print("Random Forest Price:", rf_price[0])