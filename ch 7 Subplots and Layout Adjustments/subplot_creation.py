
#! Easy Way to Create subplots
# Syntax: plt.subplot(nrows,ncols,index)
# ? Index starts from 1

import matplotlib.pyplot as plt
# !  First Chart 
x=[1,2,3,4]
y=[10,20,15,25]
plt.subplot(1,2,1)  #? 1st row , 2nd Col , 1st subplot
plt.plot(x,y)
plt.title("Line Chart")

# !  Second Chart
# Both Charts are on same Canvas

plt.subplot(1,2,2)   #? 1st row , 2nd Col , 2nd subplot

plt.bar(x,y)
plt.title("Bar Chart")
plt.show()


