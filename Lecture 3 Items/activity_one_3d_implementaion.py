## Activity 3.1 Lecture 3 
## 3D implementation

##IMPORTS
import matplotlib.pyplot as plt #imports this as plt

ax = plt.axes(projection = '3d')
ax.scatter (1, 1, 1) #creates a point at (1, 1, 1)
ax.plot([1, 5], [2, 4], [3, 3]) #creates a line that along the x plane goes from 1 to 5; along the y plane goes from 3 to 3; and along the z plane goes from 2 to 4
