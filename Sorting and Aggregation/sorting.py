import pandas as pd

data={
    "Name":['ram','shrya','xyz','pqr','abc','raj','riya'],
    "Age":[28,37,18,19,23,36,28],
    "Salary":[50000,40000,90000,60000,780000,580000,80000],
    "Performanance_Score":[89,67,78,89,67,89,98]
}

df=pd.DataFrame(data)
df.sort_values(by="Age", ascending=True, inplace=True)
print("Ascending")
print(df)

df1=pd.DataFrame(data)
df1.sort_values(by=["Age","Salary"], ascending=[True,False], inplace=True)
print("Decending")
print(df)

