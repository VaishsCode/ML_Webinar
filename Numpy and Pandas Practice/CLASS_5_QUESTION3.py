import pandas as pd 

df = pd.read_csv("students_raw.csv")

print(df.shape)
print(df.info())
print(df.describe())