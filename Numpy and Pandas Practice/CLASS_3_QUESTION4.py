"""CLASS 03 · 22
BEFORE THURSDAY
1. Create an array of 20 random exam marks between 0 and 100 with
max, min and standard deviation.
np.random.randint
, then print mean,
2. Use a boolean mask to print only the marks above the mean, and count them.
3. Build
np.arange(20).reshape(4, 5)
. Print its second column, its last row, and its column means.
4. Subtract the column means from every row in one line, and explain in a sentence why that works.
Post your notebook in the group. If something errors, post the error too — reading other people's errors is half of
learning this.
Thursday: Pandas, on a file I have broken on purpose."""

import numpy as np

arr = np.random.randint(0, 100, size=20)

print(arr)

mean = arr.mean()

print("Mean : ", mean)


print("Maximum : ", arr.max())
print("Minimum : ", arr.min())
print("Standard Deviation : ", arr.std())

mask = arr > mean

print("Boolean Mask : ", mask)
print("Marks above mean : ", arr[mask])
print("Count above mean : ", mask.sum())

arr1 = np.arange(20).reshape(4, 5)

print(arr1)

print("Second Column : ", arr1[:, 1])
print("Last Row : ", arr1[3, :])

col_mean = arr1.mean(axis=0)

print("Mean of column is : ", col_mean)

print("-----"*20)


print("MEAN CENTERING")

print("Subtraction of column means from every row is : \n", arr1 - col_mean)
