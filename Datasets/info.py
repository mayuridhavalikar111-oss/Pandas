import pandas as pd

data={
    "Name":['XYZ','ABC','PQR'],
        "Age":[10,20,30],
        "City":['fdg','yru','vbh']
}

df=pd.DataFrame(data)

print("Displaying the info of data set")
print(df.info())
#Summary