import numpy as np

marks = np.array([45,82,67,91,38,74,59,88])

marks1 = marks>=60

print(marks1)

print(marks[marks1])

print(len(marks[marks1]))

avg = marks[marks1].mean()

print(avg)

print(marks[(marks>=60) & (marks<85)])