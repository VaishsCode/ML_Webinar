import pandas as pd

# 1. Build the table (DataFrame)
df = pd.DataFrame({
    "hours_studied": [5, 2, 7],
    "attendance":    [90, 60, 85],
    "branch":        ["CS", "IT", "CS"],
    "passed":        ["Yes", "No", "Yes"],
})

print("=== Full table ===")
print(df)

# 2. Selecting columns
print("\n=== One column (Series) ===")
print(df["hours_studied"])
print(type(df["hours_studied"]))

print("\n=== Two columns (DataFrame) ===")
print(df[["hours_studied", "attendance"]])
print(type(df[["hours_studied", "attendance"]]))

# 3. Selecting rows: loc vs iloc
print("\n=== loc[0] (by label) ===")
print(df.loc[0])

print("\n=== iloc[0] (by position) ===")
print(df.iloc[0])

print("\n=== One cell: loc[0, 'branch'] ===")
print(df.loc[0, "branch"])

# 4. After filtering, labels and positions stop matching
passed_df = df[df["passed"] == "Yes"]

print("\n=== Filtered table (only passed) ===")
print(passed_df)
print("Index is now:", list(passed_df.index))

print("\n=== passed_df.loc[2] (label 2) ===")
print(passed_df.loc[2])

print("\n=== passed_df.iloc[1] (second row by position) ===")
print(passed_df.iloc[1])

# These two cause errors, so we catch them to show the message
try:
    passed_df.loc[1]
except KeyError as e:
    print("\nloc[1] -> KeyError: no row has label", e)

try:
    passed_df.iloc[2]
except IndexError as e:
    print("iloc[2] -> IndexError:", e)

# 5. value_counts()
print("\n=== passed.value_counts() ===")
print(df["passed"].value_counts())

print("\n=== branch.value_counts() ===")
print(df["branch"].value_counts())