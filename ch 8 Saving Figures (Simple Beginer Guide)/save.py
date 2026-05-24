
# ! To Save out viasuatlization 
#  Syntax: savefig('filename_+_extension',dpi=value,bbox_inches='tight')
"""
Name + Formate: plot.png
dpi value:Image resolution [Dots pr Inch]

bbox_inches: Reduce white spaces from the box side

"""

import  matplotlib.pyplot as plt

x=[1,2,3,4]
y=[10,20,15,25]

# ? Create plot
plt.plot(x,y,color='blue',marker='o')
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# ! Always save file before show
# ! Dpi=300 use for Publish or report 
# ! bbox_inches='tight' means automatically reduce white spaces
plt.savefig('line_plot.png',dpi=300,bbox_inches='tight')

# ? For Save In Folder
plt.savefig('folder_name/line_plot.png',dpi=300,bbox_inches='tight')

# print("Succesful")

plt.show()