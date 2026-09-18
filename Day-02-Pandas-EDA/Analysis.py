import pandas as pd
import numpy as np

df = pd.read_csv("./Data/employee_data.csv")
# Load the Data
print(df)

#Missing values
missing=df.isnull().sum()
print(missing)
#Average salary
Average=df['Salary'].mean()
print("Average Salary:", Average)

#Average performance
Average_Performance=df['Performance'].mean()
print("Average Performance:", Average_Performance)

#Employees with salary > 40,000
Employee_Salary=df['Salary'] > 40000;
print("Employees with salary > 40000:\n", df[Employee_Salary])


#Highest-paid employee
Hihest_Paid_Employeee=df[df['Salary'] == df['Salary'].max()]
print("Highest Paid Employee:", Hihest_Paid_Employeee)

#Employees with performance > 80
Employee_p=df['Performance'] > 80
print("Employees with performance > 80:\n", df[Employee_p])

#Average salary by department
Average_Salary_Dept=df.groupby('Department')['Salary'].mean()
print("Average Salary by Department:\n", Average_Salary_Dept)

#Sort employees by salary
Sort_emp=df.sort_values(by='Salary',ascending=False)
print("Employees sorted by salary:\n", Sort_emp)

#Fill missing salary
df['Salary']=df['Salary'].fillna(df['Salary'].mean())
print("Salary after filling missing values:\n", df['Salary'])


#Fill missing experience
df['Experience']=df['Experience'].fillna(df['Experience'].mean())
print("Experience after filling missing values:\n", df['Experience'])

def Performance():
    for i in range(len(df)):
        if df['Performance'][i] >= 80:
            df['Performance'][i] = 'Excellent'
        elif df['Performance'][i] >= 60:
            df['Performance'][i] = 'Good'
        else:
            df['Performance'][i] = 'Average'
