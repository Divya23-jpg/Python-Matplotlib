"""
? Define
A bar chart (or bar graph) is a visual representation of data using rectangular bars.
Each bar’s length or height is proportional to the value it represents.
Bars can be displayed vertically or horizontally.

? Why we use Bar charts:
1.Compare categories: Show differences between groups (e.g., revenue by product line).
2.Spot trends: Quickly highlight which category is growing or shrinking.
3.Detect outliers: Identify unusual values that stand out.
4.Communicate clearly: Convert raw numbers into visuals that non-technical stakeholders can understand.
5.Summarize large datasets: Condense complex tables into simple visuals.

"""

import matplotlib.pyplot as plt


# ? For Vertical Bars
#! plt.bar(a,height,color='name',lable='label name')
# ? For Horizontal Bars
# ! plt.barh(a,height,color='name',lable='label name')
products=['A','B',"C",'D']
sales=[1000,1500,800,1200]

# plt.bar(products,sales,color='Orange',label='Sales 2025')
plt.barh(products,sales,color='Orange',label='Sales 2025')
plt.xlabel("Products List")
plt.ylabel("Number of Sales")
plt.title("Product Sales Comparision")
plt.legend()
plt.show()
