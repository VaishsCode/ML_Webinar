import numpy as np

m = np.array([[1, 2, 3], [4, 5, 6]])  # shape (2, 3)
m + 10  # the 10 is stretched to every cell
# [[11 12 13]
#  [14 15 16]]
col_means = m.mean(axis=0)  # [2.5 3.5 4.5]  shape (3,)
centered = m - col_means  # (2,3) - (3,) works
print(centered)
