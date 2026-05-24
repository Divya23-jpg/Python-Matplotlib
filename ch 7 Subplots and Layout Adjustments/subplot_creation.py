
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
# plt.show()


# ! 2nd Way
# ? Syntax: fig,ax=plt.subplots(nrows,ncols,figsize=[width,height])

fig,ax=plt.subplots(1,2,figsize=(10,5))
x=[1,2,3,4]
y=[10,20,15,25]
ax[0].plot(x,y)
ax[0].set_title("Line Plot")

ax[1].bar(x,y)
ax[1].set_title("Bar Plot")

plt.tight_layout()
plt.show()