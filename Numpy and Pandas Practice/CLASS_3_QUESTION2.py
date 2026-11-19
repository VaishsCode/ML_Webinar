"""CLASS 03 · 09
YOUR TURN  ·  4 MINUTES
ASK THE ARRAY THREE QUESTIONS
marks = np.array([45, 82, 67, 91, 38, 74, 59, 88])
1. How many students scored 60 or above?
2. What is the average of only those scores?
3. Print the scores that are 60 or above but below 85.
No loops. No
if
. One line each."""

import numpy as np

marks = np.array([45, 82, 67, 91, 38, 74, 59, 88])

print(f"Total students scored 60 or above are : {(marks>=60).sum()}")

print(
    f"Average of scores of students scored 60 or above are : {marks[marks>=60].mean()}"
)

print(f"Students who are 60 or above but below 85 : {marks[(marks>=60) & (marks<85)]} ")
