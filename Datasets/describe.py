"""describe method : summary of discriptive statistics for numerical cloumn in a dataframe"""


import pandas as pd

data={
    "Name":['ram','shrya','xyz','pqr','abc','raj','riya'],
    "Age":[28,37,18,19,23,36,28],
    "Salary":[50000,40000,90000,60000,780000,580000,80000],
    "Performance_Score":[89,67,78,89,67,89,98]
}

df= pd.DataFrame(data)
print("Sample DataFrame")
print(df)

print("Descriptive Statistics")
print(df.describe())

'''
count- the number of non missing values in each column
mean- average of all values in each column
std- standard deviation , it tell us how much value in the column is ask rate out or different from the mean(average)
-small std- number is very close to the average
-large std- number is very different or large difference 
min- minimum value in the dataset or column

'''