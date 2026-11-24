import numpy as np 
import pandas as pd 

m = np.arange(12).reshape(3,4)

print(m)

m = (m - m.mean(axis=0))/m.std(axis=0)

print(m)