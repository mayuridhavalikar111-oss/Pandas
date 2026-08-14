import pandas as pd

df=pd.read_json("D:\Pandas\Datasets\sample_Data.json")
print("Displaying the info of the data set")
print(df.info())


data={
    "Name":['XYZ','ABC','PQR'],
        "Age":[10,20,30],
        "City":['fdg','yru','vbh']
}

df=pd.DataFrame(data)

print("Displaying the info of data set")
print(df.info())
#Summary