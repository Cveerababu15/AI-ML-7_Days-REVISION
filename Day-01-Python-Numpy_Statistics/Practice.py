import pandas as pd
import numpy as np

df = pd.read_csv("./Data/sales.csv")

# Total Sales
total_sales = df["Revenue"].sum()
print("Total Sales:", total_sales)

# Average Sales
average_sales = df["Revenue"].mean()
print("Average Sales:", average_sales)

# Highest Sale
highest_sale = df["Revenue"].max()
print("Highest Sale:", highest_sale)

# Lowest Sale
lowest_sale = df["Revenue"].min()
print("Lowest Sale:", lowest_sale)

# Number of days above average
days_above_average = (df["Revenue"] > average_sales).sum()
print("Days Above Average:", days_above_average)

# Number of days below 1000
days_below_1000 = (df["Revenue"] < 1000).sum()
print("Days Below 1000:", days_below_1000)


def analyze_sales(sales):
    sales = np.array(sales)

    average_sales = np.mean(sales)

    return {
        "Total Sales": np.sum(sales),
        "Average Sales": average_sales,
        "Highest Sale": np.max(sales),
        "Lowest Sale": np.min(sales),
        "Days Above Average": np.sum(sales > average_sales),
        "Days Below 1000": np.sum(sales < 1000)
    }


result = analyze_sales(df["Revenue"])

print("\n--- Sales Analysis Using Function ---")

for key, value in result.items():
    print(f"{key}: {value}")