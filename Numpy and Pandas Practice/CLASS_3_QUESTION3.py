"""CLASS 03 · 15
YOUR TURN  ·  4 MINUTES
THE ONE THAT MATTERS
m = np.arange(12).reshape(3, 4)
1. The mean of each column.
2. The sum of each row.
3. Subtract the column means from every row — in one line.
If you get question 3, you have understood both broadcasting and axes. That is the whole class.
"""

import numpy as np

m = np.arange(12).reshape(3, 4)

print(m)

print(f"The mean of each column is : {m.mean(axis=0)}")

print(f"The sum of each row is : {m.sum(axis=1)}")

print(
    f"The result of subtraction of column means from every row is :\n {m-(m.mean(axis=0))}"
)
