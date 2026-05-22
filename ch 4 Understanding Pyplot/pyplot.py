"""Pyplot in Matplotlib is a module that provides a simple, MATLAB-like
interface for creating plots and visualizations. 
It acts as a collection of functions that let you build and customize figures step by step, making plotting in Python straightforward and intuitive
"""
# ? Most Imp: Without data ploting cannot possible
# ! Line Grapg for Cakes Sales per Week Day 
import matplotlib.pyplot as plt

x=['Mon','Tue','Wed','Thu','Fri'] # X- Axis
y=[10,15,7,20,12] # Y-Axis
plt.plot(x,y)
plt.title("Bakery Sales This Week")
plt.xlabel("Day of the Week")
plt.ylabel("Number of Cake Sale")
plt.show()



