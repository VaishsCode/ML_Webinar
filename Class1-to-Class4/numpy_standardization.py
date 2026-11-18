"""NORMALISE A TABLE BY HAND
m = np.arange(12).reshape(3, 4)
1. Subtract each column's mean from every row.
2. Then divide by each column's standard deviation (
m.std(axis=0)
).
3. Check your answer: every column should now have a mean of about 0.
One line for step 1 and 2 together, if you can."""

import numpy as np

m = np.arange(12).reshape(3, 4)

print(m)
print("-" * 100)

m = (m - m.mean(axis=0)) / m.std(axis=0)

print(m)
