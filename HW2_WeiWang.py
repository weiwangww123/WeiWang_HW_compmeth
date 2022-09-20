# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:32:27 2022

@author: wwang3
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x):       #define the function exp(-t**2)
    return np.exp(-x**2)


x=np.arange(0,3,0.1) # define array for x
a=0.0
b=x
N=100 # number of slices
h=(b-a)/N

# use Tranpezoidal rule to calculate the integration
s=0.5*f(a)+0.5*f(b)
for k in range(1,N):
    s+=f(a+k*h)
F_trap=h*s

# use Simpsons rule to calculate the integration
s1=f(a)+f(b)
for i in range(1,int(N/2)):
    s1+=4*f(a+(2*i-1)*h)
for j in range(1,int(N/2-1)):
    s1+=2*f(a+2*j*h)
F_sim=s1*h/3

# figure of integral with x
plt.plot(x,F_trap)
plt.title("Tranpezoidal rule")
plt.xlabel("x")
plt.ylabel("E(x)")
plt.show()

plt.plot(x,F_sim)
plt.title("Simpsons rule")
plt.xlabel("x")
plt.ylabel("E(x)")
plt.show()