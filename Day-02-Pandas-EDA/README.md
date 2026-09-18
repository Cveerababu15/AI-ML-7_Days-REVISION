# Day 2 — Pandas, Data Cleaning and Employee Analytics

## Overview

Day 2 of my AI/ML revision journey focused on practising Pandas with an employee dataset.

The main focus was loading structured data, checking missing values, calculating statistics, filtering employees, grouping data by department, sorting records and handling missing values.

---

## Topics Practised

### Pandas

- `read_csv()`
- DataFrame
- Selecting columns
- `isnull()`
- `sum()`
- `mean()`
- `max()`
- Boolean filtering
- `groupby()`
- `sort_values()`
- `fillna()`

### Data Cleaning

- Checking missing values
- Filling missing salary values
- Filling missing experience values

### Data Analysis

- Average salary
- Average performance
- Highest-paid employee
- Employees with salary above 40,000
- Employees with performance above 80
- Average salary by department
- Sorting employees by salary

### Python

- Functions
- `for` loop
- `if`, `elif`, `else` conditions

---

# Project — Employee Analytics

## Objective

The objective of this project was to analyse employee data using Pandas and practise basic data cleaning and analysis operations.

The dataset contains employee-related information such as:

- Employee ID
- Department
- Age
- Salary
- Experience
- Performance

---

# Work Completed

## 1. Load Employee Data

Loaded the employee CSV file using Pandas.

```python
df = pd.read_csv("./Data/employee_data.csv")