import pandas as pd

data = pd.read_csv("students_raw.csv")

print(data)
print("-" * 100)

print(data.head())  # -> by default 5
print("-" * 100)

print(data.tail())  # -> by default 5
print("-" * 100)

print(data.info())
print("-" * 100)

print(data.describe())
print("-" * 100)

print(data["student_name"])
print("-" * 100)

print(data["student_name"].head())
print("-" * 100)

print(data["student_name"].tail())
print("-" * 100)

print(data[["student_name", "passed"]])
print("-" * 100)

print(data[["student_name", "passed"]].head())
print("-" * 100)

print(data[["student_name", "passed"]].tail())
print("-" * 100)
