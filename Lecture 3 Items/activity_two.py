## Activity 3.2 Lecture 3 
## 2D Transformation
## Create an earth rotating around the sun using Homogeneous Representation

##IMPORTS
import matplotlib.pyplot as plt #imports drawing tools as plt
import numpy as np #enables complex math

#setting up figure
fig = plt.figure (figsize = (6, 6))
ax = plt.subplot(111)
ax.set_xlim((-2, 2)) #changes the view area of the graph
ax.set_ylim((-2, 2)) #changes the view area of the graph
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('earth movement with transformation')

#representing the earth and sun
sun, = ax.plot([0], [0], 'r.', ms = 50)
earth = np.array([[0, 0], [1, 1.2], [1, 1]])
t = np.identity(3)
n_step = 1000
delta_theta = 0.01
earth_loc, = ax.plot(earth[0, 0], earth[1, 0], 'g.', ms = 20)
earth_orient, = ax.plot(earth[0, :], earth[1, :], 'g', lw = 2)
#must update earth_loc and earth_orient to visualize movememt
earth_loc.set_data(np.cos(delta_theta), -(np.sin(delta_theta)))
earth_orient.set_data(np.sin(delta_theta), np.cos(delta_theta))

#to visualize the movement
def update_draw(frames, earth_poses):
    pose = earth_poses[frames]
    earth_loc.set_data(pose[0, 0], pose[1, 0])
    earth_orient.set_data(pose[0, :], pose[1, :])
    return (earth_orient,)    
from matplotlib import rc
from matplotlib import animation
#blit = True redraws only the parts that have changed
anim = animation.FuncAnimation(fig, update_draw, frames=n_step, fargs=(trans,), interval=20, blit=True)
#equivalent to rcParams ['animation.html'] = 'html5'
rc('animation', html = 'html5')
anim
