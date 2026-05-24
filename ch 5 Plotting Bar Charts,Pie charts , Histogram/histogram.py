"""


? Definition:  
A histogram is a type of chart that represents the distribution of numerical data.
1.Data is grouped into intervals (bins).
2.Each bar shows the frequency (count) of values falling within that interval.
3.Unlike bar charts, histograms deal with continuous data, not categories.

? Why Analysts Use Histograms
1.Understand distribution: Shows how data is spread (normal, skewed, uniform, etc.).
2.Detect patterns: Identify central tendency, spread, and shape of data.
3.Spot outliers: Quickly see unusual values outside the main distribution.
4.Support statistical analysis: Useful in probability, regression, and quality control.

# ? use when numerical continious data we have
"""
import matplotlib.pyplot as plt
# bins : ranges or frequency dividedd python automatically when we give no of range
# ! plt.hist(data,bins=[num of bins],color='color name',edgecolor='colour')

scores=[45,67,89,56,78,88,92,60,74,81,59,66,75,82,90,85,70,73,68,77]
plt.hist(scores,bins=5,color='purple',edgecolor='black')
plt.xlabel("Scores Range")
plt.xlabel("Number of students")
plt.title("Score Distribution")
plt.show()
