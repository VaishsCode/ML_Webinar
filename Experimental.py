import numpy as np
data = np.genfromtxt("students.csv", delimiter=",", skip_header=1)
print(data.shape)                  # (200, 4)
hours      = data[:, 0]            # column 0 = one feature
attendance = data[:, 1]
prev_marks = data[:, 2]
passed     = data[:, 3]            # the answer column
print(hours[passed == 1].mean().round(2))   # 6.68
print(hours[passed == 0].mean().round(2))   # 3.42