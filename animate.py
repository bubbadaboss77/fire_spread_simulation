import matplotlib.pyplot as plt
import numpy as np

#plot the number of trees on fire over time
plt.figure(figsize=(6,6))
plt.plot(t,number_of_2)
plt.title('Number of trees on fire over time:')
plt.xlabel('time')
plt.ylabel('number of trees on fire')

#shape of our lattice (final_arr)
#useful for animating our plot over time
print(final_arr.shape)


from matplotlib import animation, rc
from IPython.display import HTML
import matplotlib.pyplot as plt


matplotlib.rcParams['animation.writer'] = 'avconv'
%matplotlib inline

#First set up the figure, the axis, and the plot element we want to animate
import matplotlib as mpl

#color map: white=empty tree, green=tree, red=tree on fire
cmap = mpl.colors.ListedColormap(['white', 'green', 'red'])
fig, ax = plt.subplots(figsize=(7,5))

ax.set_xlim((0,300))
ax.set_ylim((0,300))

im = ax.imshow(final_arr[0, :, :], vmin=0, vmax=2, cmap=cmap, aspect='auto')

cbar = fig.colorbar(im, ticks=np.arange(0,3))
#set color bar ticks
cbar.ax.set_yticklabels(['0', '1', '2'])

#initialize our data
def init():
    im.set_data([[], []])
    return (im,)

#animate(j) is a function that gets called iteratively.
#this function iterates through our final array and sets the data to equal each iteration
def animate(j):
    im.set_data(final_arr[j,:,:])
    return (im,)

#use animation.FuncAnimation class to animate the spread of fire over time
# number of frames must be less than length of array
#interval = time between frames
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=90, interval=150, blit=True)

anim.save('final_burn.mp4')
