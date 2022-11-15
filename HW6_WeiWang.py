# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 16:44:11 2022

@author: wwang3
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

'''
Make a video of 2D Brownian motion. Started from middle, move random to up, down , left and right.
when move to the boundary it will reflect. The movie file name is Brownian
'''
# define a funciton of 1D Brownian motion
def Brownian(N):
    '''
    1D brownian motion function. 
    
    Parameters
    ----------
    N : TYPE int
        DESCRIPTION. number of steps

    Returns
    -------
    a : TYPE 1D array
        DESCRIPTION. position of the particle

    '''
    x=0 # initial position
    a=np.zeros(N) # initial position array
    for i in range(N):
        a[i]=x # position at i step
        s=np.random.choice([-1,0,1])# move to left, right or stay rest
        x+=s
        # at the boundary it reflect
        if x>50:
            x=x-1
        elif x<-50:
            x=x+1
    return a

N=int(input("How many steps do you want in motion?:")) # move N steps
x1=Brownian(N) # move in x direction
y1=Brownian(N) # move in y direction
str1="Brownian motion "+str(N)+" steps" # figure title
# draw animation
fig = plt.figure(figsize=(5,5)) # initial figure


# define animate function to draw animation
def animate(i):
    '''
    draw animaiton figure

    Parameters
    ----------
    i : TYPE int
        DESCRIPTION. index of x,y

    Returns
    -------
    point : TYPE 
        DESCRIPTION. figure at i step

    '''
    x = x1[0:i]
    y = y1[0:i]
    point=plt.plot(x,y,"b",linewidth=0.5)
    plt.title(str1)
    plt.xlabel("x")
    plt.ylabel("y")
    return point


anim = animation.FuncAnimation(fig, animate, frames=N, interval=20, blit=True)
#save as a gif
writergif = animation.PillowWriter(fps=3)
anim.save('Brownian.gif',writer=writergif)

