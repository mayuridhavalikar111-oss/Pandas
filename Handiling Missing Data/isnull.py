import pandas as pd

data={
    "Name":[None,'shrya','xyz','pqr','abc','raj','riya'],
    "Age":[28,37,18,19,23,36,28],
    "Salary":[None,40000,90000,60000,780000,580000,80000],
    "Performanance_Score":[89,67,78,89,67,89,98]
}

df=pd.DataFrame(data)
print(df)

print(df.isnull())
print(df.isnull().sum()) #This will show how many values are missing
