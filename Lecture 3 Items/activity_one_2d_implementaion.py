## Activity 3.1 Lecture 3 
## 2D Implementation

##IMPORTS
import matplotlib.pyplot as plt #imports this as plt

ax = plt.axes()
points = ax.scatter(1, 1, c='Red', marker='*') #creates a point in space st (1,1)
line = ax.plot([1,5], [2,4], 'gray') #creates a line going from (1, 5) to (2, 4)
