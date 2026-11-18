import pandas as pd

cities = {
    "city": ["Ambajogai", "Jaipur", "Banaras"],
    "state": ["Maharashtra", "Rajasthan", "UttarPradesh"],
    "population": [73_975, 3_124_458, 1_198_491],
}

df = pd.DataFrame(cities)
print(df)

print(df.shape)
print(df.dtypes)

print(round((df["population"].mean()), 2))
