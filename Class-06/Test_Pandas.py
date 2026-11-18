import pandas as pd

print(pd.__version__)

marks = pd.Series([30, 40, 35], index=["Vrinda", "Ved", "Dev"])

print(marks["Vrinda"])

print(marks.mean())
