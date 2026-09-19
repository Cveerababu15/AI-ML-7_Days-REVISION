import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error,root_mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
# Load the dataset
df=pd.read_csv("./house_prices.csv")
print(df)

# X 
X=df[["Area","Bedrooms","Bathrooms","LocationScore","HouseAge"]]

# Y
Y=df[["Price"]]
Y=Y.values.ravel()  # Flatten the array to 1D for regression

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)


# Create a Linear Regression model
model=LinearRegression()

model.fit(X_train,Y_train)


# Make predictions
predictions=model.predict(X_test)
print("Predictions:", predictions)

# Evaluate the model
mae=mean_absolute_error(Y_test,predictions)


# MSE
mse=mean_squared_error(Y_test,predictions)


# RMSE
rmse=root_mean_squared_error(Y_test,predictions)


# R2 score
r2=r2_score(Y_test,predictions)

print("\n--- Linear Regression Evaluation ---")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)



# Random Forest Regressor
random_forest=RandomForestRegressor(n_estimators=100, random_state=42)

# Train 
random_forest.fit(X_train,Y_train)

# Make predictions
random_forest_pre=random_forest.predict(X_test)

print("\nPredictions from Random Forest Regressor:")
print(random_forest_pre)


# Evaluate the Random Forest model
rf_mae=mean_absolute_error(Y_test,random_forest_pre)
rf_mse=mean_squared_error(Y_test,random_forest_pre)
rf_rmse=root_mean_squared_error(Y_test,random_forest_pre)
rf_r2=r2_score(Y_test,random_forest_pre)

print("\n ____Random Forest Regressor Evaluation _____")
print("MAE:", rf_mae)
print("MSE:", rf_mse)
print("RMSE:", rf_rmse)
print("R2:", rf_r2)



# Model Comparision
print("\n Model Comparision")

print("\n--- Linear Regression Evaluation ---")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)


print("\n ____Random Forest Regression Evaluation _____")
print("MAE:", rf_mae)
print("MSE:", rf_mse)
print("RMSE:", rf_rmse)
print("R2:", rf_r2)