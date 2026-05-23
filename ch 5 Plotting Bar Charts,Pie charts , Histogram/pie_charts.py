"""
? Definition:  
A pie chart is a circular statistical graphic divided into slices to illustrate numerical proportions.
1.Each slice represents a category’s contribution to the whole.
2.The size of the slice is proportional to its percentage of the total.


? Why Analysts Use Pie Charts
1.Show proportions: Best for displaying how a dataset is split into parts.
2.Quick visualization: Easy to understand at a glance.
3.Highlight dominance: Makes it clear which category has the largest share.
4.Percentage focus: Useful when the total is 100% and categories are mutually exclusive.

"""
import matplotlib.pyplot as plt

# plt.pie(values,label='label name',color='color_list',autopct='%1.1f%%')
# ? autopct tells that how much % holds each slice
# ? %1.1f%% means 1 digit before decimal and 1 digits after decimal and %% mneans diplay % sign on a screen

regions=['North','South','East','West']
revenue=[3000,2000,1500,1000]
plt.pie(revenue,labels=regions,autopct='%1.1f%%',colors=['gold','skyblue','lightgreen','coral'])
plt.title("Revenue Contribution By Region")

plt.show()