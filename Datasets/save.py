import pandas as pd

data={
    "Name":['XYZ','ABC','PQR'],
    "Age":[10,20,30],
    "City":['fdg','yru','vbh']
}

df=pd.DataFrame(data)
print(df)

#df.to_csv("output.csv",index=False) #encoding='utf-8
#df.to_excel("output.xlsx", engine = "openpyxl")
df.to_json("output.json",index=False)
