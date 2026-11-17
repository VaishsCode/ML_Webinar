import numpy as np

m = np.array([[1, 2, 3],
[4, 5, 6]])
print(m.shape)   # (2, 3)  -> 2 rows, 3 columns
print(m.ndim)    
# 2       
print(m.dtype)   # int64   -> whole numbers
print(m.size)    
# 6       -> it is a matrix, not a vector-> total elements