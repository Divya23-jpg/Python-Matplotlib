import matplotlib.pyplot as plt

# 1. plt.plot(): Used for line graph
# ! plt.plot(x, y, colour='color name', linestyle='Line_style', linewidth=value, marker='marker symbol',label='label name')



months=[1,2,3,4,5]
sales=[1000,1500,2000,4000,1200]

plt.plot(months,sales,color='blue',linestyle='--', linewidth=2,marker='o',label='2025 Sales Data')

# 2.plt.xlabel(): used for label on a X-axis 
# ! plt.xlabel('text)
# 3.plt.ylabel(): used for label on a Y-axis 
# ! plt.ylabel('text)

plt.xlabel('Number of Months')
plt.ylabel('Number of Sales per month')

# 4 plt.title() : used to show heading of the graph
# ! plt.title('text')
plt.title('Monthly Sales Data Report')


# 5 plt.legend(): used to show small box and tell which marker and line presents
# ! plt.legend(loc='location,font size=value): Parameters are fully optional
# ? loc='upper left'  loc='lower left'
# ? Legend only see when we add Label
plt.legend(loc='upper left',fontsize=12)

# 6 plt.grid(): used to show boxes in the area of graph
# ! plt.grid(color='colur name',linestyle='style',linewidth=value):
plt.grid(color='grey',linestyle=':',linewidth=1)


#  7 plt.xlim(str,end): used to limit X Axis
#  7 plt.ylim(str,end): used to limit y Axis
# ! plt.xlim(start,end)  and  plt.ylim(start,end)

plt.xlim(1,4)
plt.ylim(0,2000)

# ! plt.xticks(old,new): used to replace labeling  x points 
# ! plt.yticks(old,new): used to replace labeling y points 
plt.xticks([1,2,3,4,5], ['M1','M2','M3','M4','M5'])

# plt.show(): T0 display a plot on the screen
plt.show()