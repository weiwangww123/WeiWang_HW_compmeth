# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 18:47:05 2022

@author: wwang3
"""

import numpy as np
from astropy.constants import M_earth,G
import matplotlib.pyplot as plt

# define the function based on newton's equation
def f(x):
    """
    This function is to use the right term of the newton's equation minus the left
    term. we have define the mass of moon, the distance between the moon and the
    earth, the orbit frequency, the mass of the earth and G.
    """
    M_moon=7.348e22 # the mass of the moon
    R=3.844e8 # the distance of the moon and the earth
    w=2.662e-6 # the orbit frequency
    f=x-(G.value*M_earth.value/x**2-G.value*M_moon/(R-x)**2)*10**(12)/(2.662)**2
    return f

# define the ratio of f(x) and its derivative
def F(x):
    """
    This function is to define the derivative of f(x) and return the
    ratio of f(x) and the derivative
    """
    M_moon=7.348e22
    R=3.844e8
    w=2.662e-6
    f=x-(G.value*M_earth.value/x**2-G.value*M_moon/(R-x)**2)*10**(12)/(2.662)**2
    df=1+2*G.value*M_earth.value/x**3/w**2+2*G.value*M_moon/(R-x)**3/w**2
    return f/df

M_moon=7.348e22 # the mass of the moon
R=3.844e8 # the distance of the moon and the earth
w=2.662e-6 # the orbit frequency

# draw the figure of f(x) to see where the root is
h=np.linspace(0.1,0.9,100)*R
plt.plot(h/R,f(h))
plt.xlabel("r/R")
plt.ylabel("f(r)")

# use the newton's method to find the root of the equation
x0=0
x=0.9*R # starting value
eps=0.0001 # the accuracy

while np.abs(x-x0)>eps:
    x0=x
    x=x0-F(x0)

# use the secant method to find theroot of the equation
x1=0.9*R # starting value 1
x2=0.89*R # starting value 2
x3=0

while np.abs(x3-x2)>eps:
    x3=x2-f(x2)*(x2-x1)/(f(x2)-f(x1))
    x1=x2
    x2=x3

# print the roots from two methods
print("the Lagrange point from Newton's method is ",x/R,"*R")
print("the Lagrange point from Secant method is ",x3/R,"*R")