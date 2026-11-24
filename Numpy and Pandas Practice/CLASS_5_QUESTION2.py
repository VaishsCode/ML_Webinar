import pandas as pd

df = pd.read_csv("students_raw.csv")

print(df.head(10))

print("-" * 20 + "unique spellings of branch" + "-" * 20)

print(df["branch"].nunique())

print("-" * 20 + "rows are exact duplicates" + "-" * 20)

print(df.duplicated().sum())

print("-" * 20 + "highest value in hours studied" + "-" * 20)

print(df["hours_studied"].max())

print("-" * 20 + "index of highest value in hours studied" + "-" * 20)

print(df["hours_studied"].idxmax())

print("-" * 20 + "row of highest value in hours studied" + "-" * 20)

inx_max = df["hours_studied"].idxmax()

print(df.loc[inx_max])
