import pandas as pd

data={
    "Name":['ram','shrya','xyz','pqr','abc','raj','riya'],
    "Age":[28,37,18,19,23,36,28],
    "Salary":[50000,40000,90000,60000,780000,580000,80000],
    "Performanance_Score":[89,67,78,89,67,89,98]
}

df=pd.DataFrame(data)
print(df)

#.loc[]
#df.loc[row_index, "Column Name"]=new_value

df.loc[0,"Salary"]=55000     #It will change the salary of ram to 55000
print(df)

#Updating multiple values
df["Salary"]=df["Salary"]=1.05
print(df)
