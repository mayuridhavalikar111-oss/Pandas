import pandas as pd

data={
    "Name":['ram','shrya','xyz','pqr','abc','raj','riya'],
    "Age":[28,37,18,19,23,36,28],
    "Salary":[50000,40000,90000,60000,780000,580000,80000],
    "Performanance_Score":[89,67,78,89,67,89,98]
}

df=pd.DataFrame(data)
print(df)

#Adding columns via assignment
df["Bonus"]= df["Salary"]*0.1
print(df)

#Using insert() method
df.insert(2, "Employee ID",[10,20,30,40,50,60,70])
print(df)

