#For removing missing values - dropna()
#df.dropna(axis=0, inplace=True)  axis=0 - rows missing value

#df.dropna(axis=1, inplace=True)  axis=1 - coloumn missing values


import pandas as pd

data={
    "Name":[None,'shrya','xyz','pqr','abc','raj','riya'],
    "Age":[28,37,18,19,23,36,28],
    "Salary":[None,40000,90000,60000,780000,580000,80000],
    "Performanance_Score":[None,67,78,89,67,89,98]
}

df=pd.DataFrame(data)
print(df)
df.dropna(axis=0, inplace=True) 



#For filling the missing values - fillna()
#fillna(value, inplace-True)  the missing data will get replaced by the given value

df.fillna(0, inplace=True)
print(df)


df["Salary"].fillna(df["Salary"].mean(), inplace=True)
print(df)

