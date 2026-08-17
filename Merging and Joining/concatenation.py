'''
vertically(row)
horizontally(column)

pd.concate([df1, df2],axis=0, ignore_index=True)
'''


import numpy as pd

#Region 1
df_Region1=pd.DataFrame({
    'CoustomerID':[1,2,3],
    'Name':["ABC","XYZ","PQR"]
})

#Region 2
df_Region2=pd.DataFrame({
    'CoustomerID':[4,5,6],
    'Name':["abc","xyz","pqr"]
})

#Vertically
df_concat=pd.concat([df_Region1,df_Region2],ignore_index=True)
print(df_concat)


#Horizontaly
df_concat=pd.concat([df_Region1,df_Region2],axis=1,ignore_index=True)
print(df_concat)
