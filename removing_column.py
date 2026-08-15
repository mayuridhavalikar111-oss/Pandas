import pandas as pd

data={
    "Name":['ram','shrya','xyz','pqr','abc','raj','riya'],
    "Age":[28,37,18,19,23,36,28],
    "Salary":[50000,40000,90000,60000,780000,580000,80000],
    "Performanance_Score":[89,67,78,89,67,89,98]
}

df=pd.DataFrame(data)
print(df)

#Removing single column
#df.drop(columns=["ColumnName"], inplace=True)
print("After removing a column")
df.drop(columns=["Performanance_Score"], inplace=True)
print(df)

'''
#Removing multiple columns
df.drop(columns=["Performanance_Score","Age"], inplace=True)
print(df)
'''