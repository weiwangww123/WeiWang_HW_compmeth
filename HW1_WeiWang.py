# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 17:25:17 2022

@author: wwang3
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

theta1=np.linspace(0,2*np.pi,1000)
x1=2*np.cos(theta1)+np.cos(2*theta1)
y1=2*np.sin(theta1)-np.sin(2*theta1)
plt.plot(x1,y1,color='yellow')
plt.title("deltoid curve")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

theta2=np.linspace(0,10*np.pi,1000)
x2=theta2**2*np.cos(theta2)
y2=theta2**2*np.sin(theta2)
plt.plot(x2,y2,color='blue')
plt.title("spiral curve")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

theta3=np.linspace(0,24*np.pi,1000)
r=np.exp(np.cos(theta3))-2*np.cos(4*theta3)+np.sin(theta3/12)**5
x3=r*np.cos(theta3)
y3=r*np.sin(theta3)
plt.plot(x3,y3,color='red')
plt.title("Fey's equation")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
