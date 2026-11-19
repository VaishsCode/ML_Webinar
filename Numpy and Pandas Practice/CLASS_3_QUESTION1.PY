"""CLASS 03 · 05
YOUR TURN  ·  3 MINUTES
BUILD IT AND INSPECT IT
1. Make a 1D array of 5, 10, 15 … up to 50. Do not type the numbers.
2. Reshape it into 2 rows.
3. Print its 
shape 
, 
ndim
 and 
dtype 
.
Type it yourself. Do not copy from the recording later — the muscle memory is the point."""

import numpy as np

arr = np.arange(5, 55, 5)

print(arr)

arr1 = arr.reshape(2, 5)

print(arr1)

print(arr1.shape)
print(arr1.ndim)
print(arr1.dtype)
