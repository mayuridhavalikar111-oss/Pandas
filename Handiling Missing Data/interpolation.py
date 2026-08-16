'''Interpolation is the process in which missing value is filled with the estimeted value
It follows the pattern to fill the missing value

Why interpolation is used-
1- Preserve data integrity ( missing values are replaced with arbitary number)
2- Smooth trends
3- Avoid data loss

interpolate()
Their are different methods for interpolation like linear, polynomial, time, etc'''

import pandas as pd

data={
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}
df=pd.DataFrame(data)
print("Before interpolation")
print(df)

df["Value"]=df["Value"].interpolate(method="linear")
print("After interpolation")
print(df)

'''
Where to use interpolation
1- timer series data
2- numeric data which follows trend
3- avoide droping data
'''

