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
import requests
from bs4 import BeautifulSoup

url1="http://www-personal.umich.edu/~mejn/cp/data/dow.txt"
url2="http://www-personal.umich.edu/~mejn/cp/data/dow2.txt"

Data={"dow.txt":url1,"dow2.txt":url2}
Method={"DFT":[rfft,irfft],"DCT":[dcst.dct,dcst.idct]}

parser = argparse.ArgumentParser(description="DFT and DCT of the signal")
parser.add_argument("-d","--dataFile",type=str, default ="dow.txt",help="the data file")
parser.add_argument("-p","--percent",type=float,default=0.1,help="the percent of value to keep,like 0.02 or 0.1")
parser.add_argument("-m","--method",type=str,default="DFT",help="use what kind of method? DFT or DCT")
args=parser.parse_args()

if __name__=='__main__':
    url=Data[args.dataFile]
    resp=requests.get(url)
    html=resp.text
    soup=BeautifulSoup(html,"html.parser")
    data=soup.find("pre")

    ss=soup.text
    s=ss.split("\n")
    l=len(s)
    y=np.zeros(l-1)
    for i in range(l-1):
        y[i]=float(s[i])
    
    

    #y=np.loadtxt(args.dataFile,float) # load data from file
    
    yf=Method[args.method][0](y) # use DFT method to get Fourier transform of data
    s=len(yf) # number of the value
    
    # let the value be zeros but first percent
    for i in range(math.floor(s*args.percent),s):
        yf[i]=0.0
    y1=Method[args.method][1](yf) # inverse Fourier transform the values
    
    # plot the figure of raw data, furnished data and coefficients of data using DFT method
    plt.figure(figsize=(10,5))
    
    plt.subplot(1,2,1)
    plt.plot(y,"red",label="raw data") # raw data line
    plt.plot(y1,"blue",label="furnished data") # furnished data line
    plt.xlabel("days")
    plt.ylabel("value")
    plt.legend()
    str1=args.method+" method using data from "+args.dataFile+" and keep "+str(args.percent)+" data"
    plt.suptitle(str1)
    
    
    plt.subplot(1,2,2)
    plt.plot(yf)
    plt.xlabel("k")
    plt.ylabel("coefficients of DFT")
    plt.show()
    