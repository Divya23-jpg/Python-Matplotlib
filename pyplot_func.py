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
plt.show()