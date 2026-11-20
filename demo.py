import numpy as np
import pandas as pd

print(np.__version__)
print("Hello World")

print(pd.__version__)

df = pd.read_csv("students_raw.csv")

print(df["hours_studied"])  # one column, a Series
# two columns, a DataFrame
# row by LABEL
# row by POSITION
# one cell
print("--" * 50)
print(df[["hours_studied", "attendance"]])
print("--" * 50)
print(df.loc[0])
print("--" * 50)
print(df.iloc[0])
print("--" * 50)
print(df.loc[0, "branch"])
