'''Filtering rows
Using boolean indexing
Example--
-Based on a single condition
filtered_Rows=df[df["Salary"]>50000]

-combine multiple conditions
filtered_Rows=df[(df["salary"]>50000) & (df["Column2] < 80000)]
'''

import pandas as pd

data={
    "Name":['ram','shrya','xyz','pqr','abc','raj','riya'],
    "Age":[28,37,18,19,23,36,28],
    "Salary":[50000,40000,90000,60000,780000,580000,80000],
    "Performanance_Score":[89,67,78,89,67,89,98]
}

df=pd.DataFrame(data)

#Based on single condition
high_salary=df[df["Salary"]>50000]
print("Employe with salary>50000")
print(high_salary)

#Based on multiple conditions
filtered=df[(df["Age"]>30) & (df["Salary"]>50000)]
print(f"Employe list with age>30 + salary>50000")
print(filtered)

#Using OR condition
filtered_or=df[(df["Age"]>30) | (df["Performanance_Score"]>90)]
print(f"Employe list with age>30 OR Performanance_Score>50000")
print(filtered_or)
