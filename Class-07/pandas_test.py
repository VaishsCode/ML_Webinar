import pandas as pd

df = pd.read_csv("students_raw.csv")

# hours_8 = df["hours_studied"] > 8

# print(f"Students with study hours more than 8 hrs are : {df[hours_8]}")

# print(f"There are total {len(df[hours_8])} students with study hours more than 8 hrs")

# print("--" * 100)

# failed = df["passed"] == 0

# print(f"Students who have failed are : {df[failed]}")

# print(f"There are total {len(df[failed])} students who are failed")

# print("--" * 100)

# branch_cse = df["branch"] == "C.S.E"

# print(f"Students who belong to branch C.S.E are : {df[branch_cse]}")

# print(f"There are total {len(df[branch_cse])} students who belong to branch C.S.E")

# print("--" * 100)

either = df[(df["prev_marks"] > 75) | (df["hours_studied"] > 6)]
print(either.shape[0])