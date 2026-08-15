'''Selecting columns
it returns--
1- a series (single column of data)
2- dataframe (multiple columns of data)
Example--
-Accecing single column
column=df["Column Name"]

-Accecing multiple columns
subset=df["Column1","Column2","Column3"]'''

import pandas as pd

data={
    "Name":['ram','shrya','xyz','pqr','abc','raj','riya'],
    "Age":[28,37,18,19,23,36,28],
    "Salary":[50000,40000,90000,60000,780000,580000,80000],
    "Performance_Score":[89,67,78,89,67,89,98]
}

df=pd.DataFrame(data)

#display the dataframe
#Selecting single column
print("Sample Dataframe")
print(df)
print("Names (single column return series)")
name=df['Name']
print(name)

#Selecting multiple columns
subset=df[["Name","Salary"]]
print("\nSubset with Name and Salary")
print(subset)

