"""
# ? Solve Problem:
We Cant find Patterns or Trends of a scatter data

# ? Define Scatter graph:
    It is a graph where each points represents one observation with two values (x,y)

?  Co Realations Beetween  2 variables  like Advertisemnet V/s Sales
"""

import matplotlib.pyplot as plt

# ? plt.scatter(x,y,color='color_name',marker='marker style',label='label name')
# marker means dot type or  which type of point you want to show

hours_stu=[1,2,3,4,5,6,7,8]
exam_scors=[50,55,60,65,70,75,80,85]
plt.scatter(hours_stu,exam_scors,color='Red',marker='o',label='Student Data')
plt.xlabel("Study Hours Of a Student")
plt.ylabel("Exam Scores Of a Student")
plt.title("Relation Between Study Time and Exam Scores")
plt.legend()
plt.grid('True')
plt.show()