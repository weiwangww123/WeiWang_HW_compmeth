# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 17:35:05 2022

@author: wwang3
"""

import numpy as np
import matplotlib.pyplot as plt


# define fucntion of electric potential
def Phi(x,y):
    q1=1.0
    q2=-1.0
    d=0.1 # distance between two points
    side=1.0 # length of square
    x1=side/2+d/2 # first charge
    y1=side/2
    x2=side/2-d/2 # second charge
    y2=side/2
    epsilon0=8.85*10**(-12)
    r1=np.sqrt((x-x1)**2+(y-y1)**2+0.01) # 0.01 is for r1 not equalls 0
    r2=np.sqrt((x-x2)**2+(y-y2)**2+0.01) # 0.01 is for r2 not equalls 0
    return q1/(4*np.pi*epsilon0*r1)+q2/(4*np.pi*epsilon0*r2)

side=1.0 # length of the square
h=0.01 # separation of the side
points=int(side/h) # space points
x=np.arange(0,side,h) # array for x
y=x                   # array for y
X,Y=np.meshgrid(x,y)  # 2D array for x y

# draw the figure of electric potential
plt.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=0.5,hspace=0.15)
plt.subplot(1,2,1)
plt.contourf(X,Y,Phi(X,Y),30,cmap="rainbow_r")
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Electric Potential")

# calculate the electric field
Ex=np.empty([points,points],float) # 2D array for Ex
Ey=np.empty([points,points],float) # 2D array for Ey
for i in range(points): # sweep every (x,y) points
    y=h*i
    for j in range(points):
        x=h*j
        Ex[i,j]=(Phi(x+h/2,y)-Phi(x-h/2,y))/h
        Ey[i,j]=(Phi(x,y+h/2)-Phi(x,y-h/2))/h
        
# draw the figure of electric field
plt.subplot(1,2,2)
plt.streamplot(X,Y,Ex,Ey,density=1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Electric Field")
plt.show()
