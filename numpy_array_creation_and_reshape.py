import numpy as np

a = np.arange(5, 55, 5)
print(a)
m = a.reshape(2, 5)
print(m.shape, m.ndim, m.dtype)
