# Day 1 — Python, NumPy and Statistics

## Overview

Day 1 of my AI/ML revision focuses on strengthening Python fundamentals, NumPy and basic data analysis through a simple Store Sales Analyzer project.

The main goal was to understand the concepts and write the code myself rather than simply copying a solution.

---

## Topics Practised

### Python

* Variables
* Data types
* Lists
* Dictionaries
* Conditions
* Loops
* Functions
* Basic problem solving

### NumPy

* NumPy arrays
* `np.array()`
* `np.sum()`
* `np.mean()`
* `np.max()`
* `np.min()`
* Boolean conditions

### Pandas

* Reading CSV files
* DataFrame
* Selecting columns
* Working with numerical data

### Statistics

* Mean
* Understanding average values
* Comparing values with the average

---

# Project — Store Sales Analyzer

## Objective

Build a simple Python program that reads sales data from a CSV file and performs basic sales analysis.

The program analyses the `Revenue` column and calculates important sales values.

---

## Dataset

The project uses a CSV file containing sales information.

Main columns include:

* Product
* Quantity
* Price
* Revenue
* Day

---

## Requirements Completed

The program calculates:

1. Total Sales
2. Average Sales
3. Highest Sale
4. Lowest Sale
5. Number of Days Above Average
6. Number of Days Below 1000

A reusable `analyze_sales()` function was also created to perform the same analysis.

---

## Project Structure

```text
Day-1/
│
├── main.py
├── README.md
│
└── Data/
    └── sales.csv
```

---

# How I Implemented It

## 1. Load the CSV File

I used Pandas to load the sales dataset.

```python
df = pd.read_csv("./Data/sales.csv")
```

---

## 2. Calculate Total Sales

I used the `sum()` function on the Revenue column.

```python
total_sales = df["Revenue"].sum()
```

---

## 3. Calculate Average Sales

I used the `mean()` function to calculate the average revenue.

```python
average_sales = df["Revenue"].mean()
```

---

## 4. Find Highest Sale

I used `max()` to find the highest revenue value.

```python
highest_sale = df["Revenue"].max()
```

---

## 5. Find Lowest Sale

I used `min()` to find the lowest revenue value.

```python
lowest_sale = df["Revenue"].min()
```

---

## 6. Count Days Above Average

I compared each Revenue value with the calculated average.

```python
days_above_average = (df["Revenue"] > average_sales).sum()
```

The condition produces `True` and `False` values.

The `sum()` counts the `True` values.

---

## 7. Count Days Below 1000

I compared each Revenue value with `1000`.

```python
days_below_1000 = (df["Revenue"] < 1000).sum()
```

This counts how many sales values are below 1000.

---

## 8. Create a Reusable Function

I created the following function:

```python
def analyze_sales(sales):
```

The function accepts sales data and performs the required calculations using NumPy.

The function returns the results as a dictionary.

---

# Technologies Used

* Python
* Pandas
* NumPy
* CSV

---

# What I Learned

Through this project, I practised:

* Loading CSV data using Pandas
* Working with DataFrame columns
* Performing basic calculations
* Calculating averages
* Finding maximum and minimum values
* Using Boolean conditions
* Counting matching values
* Creating Python functions
* Using NumPy arrays
* Returning multiple results using a dictionary

---

# Project Workflow

```text
CSV File
   ↓
Load Data using Pandas
   ↓
Select Revenue Column
   ↓
Calculate Sales Values
   ↓
Apply Conditions
   ↓
Analyse Sales
   ↓
Return Results
```

---

# Interview Explanation

> I built a Store Sales Analyzer using Python, Pandas and NumPy. I loaded sales data from a CSV file using Pandas and analysed the Revenue column. I calculated total, average, highest and lowest sales. I also used Boolean conditions to count the number of days above the average and the number of days below 1000. Finally, I created a reusable `analyze_sales()` function that performs these calculations using NumPy.

---

# Day 1 Status

**Completed**

### Completed Work

* Python fundamentals revision
* NumPy basics
* Pandas CSV loading
* Basic sales calculations
* Boolean conditions
* Functions
* Store Sales Analyzer

---

## Key Learning

The main concept from Day 1 was:

```text
Understand the data
        ↓
Write the logic
        ↓
Calculate the result
        ↓
Check the output
        ↓
Explain the approach
```

Day 1 completed with a practical Python + NumPy sales analysis project.
