# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 19:29:39 2022

@author: wwang3
"""

import numpy as np
import matplotlib.pyplot as plt
import math

g=9.8 # gracity constant
R=0.08 # radius of the ball
theta=30/180*np.pi # incident angle
v=100 # initial velocity
p=1.22 # the density of air
C=0.47 # the coefficient of drag

# define function to get first and second derivative
def f(r,t,m):
    '''
    define a fucntion to get first and second derivative
    at t time point and m mass

    Parameters
    ----------
    r : TYPE array
        DESCRIPTION. [x,vx,y,vy]
    t : TYPE float
        DESCRIPTION. time point
    m : TYPE float
        DESCRIPTION. mass

    Returns
    -------
    TYPE array
        DESCRIPTION. [vx,ax,vy,ay]

    '''
    A=np.pi*R**2*p*C/2/m # coefficient
    vx=r[1]
    vy=r[3]
    fx=vx
    fvx=-A*vx*(vx**2+vy**2)**(1/2)
    fy=vy
    fvy=-g-A*vy*(vx**2+vy**2)**(1/2)
    return np.array([fx,fvx,fy,fvy],float)

t0=0.0 # begin time
tend=7.0 # end time
N=100 # number of points
h=(tend-t0)/N # dt

# define fucntion to get trajectory fo the ball
def f1(tend,N,m):
    '''
    define fucntion to get trajectory fo the ball
    from t0 to tend, N points, m mass
    return the trajectory points in x and y direction

    Parameters
    ----------
    tend : TYPE float
        DESCRIPTION. end time
    N : TYPE int
        DESCRIPTION. points
    m : TYPE float
        DESCRIPTION. mass

    Returns
    -------
    xpoints : TYPE list
        DESCRIPTION. points in x direction
    ypoints : TYPE list 
        DESCRIPTION. points in y direction

    '''
    tpoints=np.arange(t0,tend,h)
    xpoints=[]
    ypoints=[]
    vxpoints=[]
    vypoints=[]
    x=0.0 # initial position
    y=0.0 # initial position
    vx=v*np.cos(theta)
    vy=v*np.sin(theta)
    for t in tpoints:
        xpoints.append(x)
        ypoints.append(y)
        vxpoints.append(vx)
        vypoints.append(vy)
        r=[x,vx,y,vy]
        k1=h*f(r,t,m)
        k2=h*f(r+0.5*k1,t+0.5*h,m)
        k3=h*f(r+0.5*k2,t+0.5*h,m)
        k4=h*f(r+k3,t+h,m)
        x+=(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
        vx+=(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
        y+=(k1[2]+2*k2[2]+2*k3[2]+k4[2])/6
        vy+=(k1[3]+2*k2[3]+2*k3[3]+k4[3])/6
    return xpoints,ypoints

eps=0.01
# define function to find travel distance
def findZeros(eps,N,m):
    '''
    define function to find travel distance
    eps is small term, N poins, m mass
    return travel distance x_1

    Parameters
    ----------
    eps : TYPE
        DESCRIPTION.
    N : TYPE
        DESCRIPTION.
    m : TYPE
        DESCRIPTION.

    Returns
    -------
    x_1 : TYPE
        DESCRIPTION.

    '''
    xpoints,ypoints=f1(tend,N,m)
    for i in range(math.floor(N/10),len(ypoints)):
        if ypoints[i]<eps:
            break
    x_1=xpoints[i]
    return x_1

m=1
xpoints,ypoints=f1(tend,N,m)


M=np.linspace(0.1,10,100)
x=[]
for i in range(len(M)):
    m=M[i]
    x2=findZeros(eps,N,m)
    x.append(x2)

print("the heavier the ball, the travel distance larger\nthe farest distance is around 600")

plt.figure(figsize=(14,7))
plt.subplot(1,2,1)
plt.plot(xpoints,ypoints)
plt.plot([0,250],[0,0])
plt.xlabel("x")
plt.ylabel("y")
plt.title("the trajectory of the 1 kg call incident in 30 degree")
plt.subplot(1,2,2)
plt.plot(M,x)
plt.xlabel("m/kg")
plt.ylabel("travel distance")
plt.show()

    
    
    