''' head() tail()'''
import pandas as pd
df=pd.read_json("Datasets\sample_Data.json")

print("Display 10 rows of first")
print(df.head(5))

print("Display 10 rows of last")
print(df.tail(10))
