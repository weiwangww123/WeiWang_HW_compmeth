# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 19:32:51 2022

@author: wwang3
"""

import numpy as np

"""
w(x)=x**(-1/2), so intergration I1 of w(x) over 0 to 1 is 2
so p(x)=w(x)/I1=x**(-1/2)/2
intergration I2 of p(x) over 0 to x is x**(1/2)
let z=I2, so x=z**2
"""

N=1000000 # number of random points
g=0 # initial value of g(x)

for i in range(N):
    z=np.random.rand() # random number between 0 and 1
    x=z**2 # x relates to z
    g+=1/(np.exp(x)+1) # sum of g(x)
I=g*2/N
print("the intergration is ",I)