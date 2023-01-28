import matplotlib.pyplot as plt
import numpy as np

#activity L3.2
#create a figure and axes
fig = plt.figure(figsize=(6,6))
ax = plt.subplot(111)

ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('earth movement with transformation')

#use two points (a vector) to represent earth orientation and location
earth = np.array([[0,0],[1,1.2],[1,1]])
t = np.identity(3)
n_step = 1000
delta_theta = 0.01

def move(t, steps):
    trans = {}
    trans[0] = t
    for i in range(steps):
        movement = np.array([[np.cos(delta_theta), np.sin(delta_theta), 0], [-np.sin(delta_theta), np.cos(delta_theta), 0], [0,0,1]])
        trans[i+1] = np.matmul(trans[i], movement)
    return trans

trans = move(t, n_step)

#movement
sun, = ax.plot([0], [0], 'r.', ms=50)
earth_loc, = ax.plot(earth[0,0], earth[1,0], 'g.', ms=20)
earth_orient, = ax.plot(earth[0,:], earth[1,:], 'g', lw=2)

#animation function this is called sequentially
def update_draw(frames, trans):
    pose = np.matmul(trans[frames], earth)
    earth_loc.set_data(pose[0,0], pose[1,0])
    earth_orient.set_data(pose[0,:], pose[1,:])
    return (earth_orient,)

#show animation
from matplotlib import rc
from matplotlib import animation

#blit=True re-draws only the parts that have changed
anim = animation.FuncAnimation(fig, update_draw, frames=n_step, fargs=(trans,), interval=20, blit=True)

#equivalent to rcParams['animation.html'] = 'html5'
rc('animation', html='html5')
anim
