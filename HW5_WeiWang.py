# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:15:30 2022

@author: wwang3
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft,irfft
import math
import dcst
import argparse

parser = argparse.ArgumentParser(description="DFT and DCT of the signal")
parser.add_argument("-d","--dataFile",type=str, default ="dow.txt",help="the data file")
parser.add_argument("-p","--percent",type=float,default=0.1,help="the percent of value to keep")
args=parser.parse_args()

if __name__=='__main__':
    

    y=np.loadtxt(args.dataFile,float) # load data from file
    
    yf=rfft(y) # use DFT method to get Fourier transform of data
    s=len(yf) # number of the value
    
    # let the value be zeros but first percent
    for i in range(math.floor(s*args.percent),s):
        yf[i]=0.0+0.0j
    y1=irfft(yf) # inverse Fourier transform the values
    
    y2=dcst.dct(y) # use DCT method to get Fourier transform of data
    s2=len(y2) # number of the value
    
    # let the value be zeros but first percent
    for i in range(math.floor(s2*args.percent),s2):
        y2[i]=0.0
    y3=dcst.idct(y2) # inverse Fourier transform the values
    
    # plot the figure of raw data, furnished data and coefficients of data using DFT method
    plt.figure(figsize=(10,5))
    
    plt.subplot(1,2,1)
    plt.plot(y,"red",label="raw data") # raw data line
    plt.plot(y1,"blue",label="furnished data") # furnished data line
    plt.xlabel("days")
    plt.ylabel("value")
    plt.legend()
    str1="DFT method using data from "+args.dataFile+" and keep "+str(args.percent)+" data"
    plt.suptitle(str1)
    
    
    plt.subplot(1,2,2)
    plt.plot(yf)
    plt.xlabel("k")
    plt.ylabel("coefficients of DFT")
    
    # plot the figure of raw data, furnished data and coefficients of data using DCT method
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.plot(y,"red",label="raw data")
    plt.plot(y3,"blue",label="furnished data")
    plt.xlabel("days")
    plt.ylabel("value")
    plt.legend()
    str2="DCT method using data from "+args.dataFile+" and keep "+str(args.percent)+" data"
    plt.suptitle(str2)
    
    plt.subplot(1,2,2)
    plt.plot(y2)
    plt.xlabel("k")
    plt.ylabel("coefficients of DCT")
    plt.show()