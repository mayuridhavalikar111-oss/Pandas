#pd.merge(df1, df2, on="Column_Name", how="Type of join")

import pandas as pd

df_coustomers=pd.DataFrame({
    'CoustomerID':[1,2,3],
    'Name':['ABC','XYZ','PQR']
})

#order dataframe
df_orders= pd.DataFrame({
    'CoustomerID':[1,2,3],
    'OrderAmount':[290,567,234]
})

#Merge
df_merged=pd.merge(df_customers, df_orders, on="CoustomerID", how="inner")
print('inner join')
print(df_merged)

#right join
#left join
#cross join

