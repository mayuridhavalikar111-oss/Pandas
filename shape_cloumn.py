'''ANALYSING dataset
1- how big is your dataset
2- what are the names of columns

shape and columns

shape -
-It is an attribute 
-Show number of row and columns in the dataset
-It is a attribute which will return tuple in which it gives 2 values-
number of rows & number of columns
-To find size of dataset

columns-
-It is an attribute
-It returns name of column as an index object (in single click it will provide all the names of columns)
-It gives all the names of columns present in the dataset
'''


import pandas as pd

data={
    "Name":['ram','shrya','xyz','pqr','abc','raj','riya'],
    "Age":[28,37,18,19,23,36,28],
    "Salary":[50000,40000,90000,60000,780000,580000,80000],
    "Performance_Score":[89,67,78,89,67,89,98]
}

df=pd.DataFrame(data)
print(df)
print(f"Shape: [df.shape]")
print(f"Column Names: {df.columns}")


