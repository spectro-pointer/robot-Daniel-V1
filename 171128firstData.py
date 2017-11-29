#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:59:34 2017

@author: Daniel
"""
import glob, matplotlib, numpy

# define a function to smooth the data
def movingAv(a,window):
    b = list(a.shape)
    b[0]=b[0]-window+1
    saver = numpy.zeros(b)
    for ind in numpy.arange(window):
        saver=saver+a[ind:a.shape[0]-window+ind+1,]
    saver=saver/window
    return saver

# get all file names for one well
files = glob.glob('/Users/home/Downloads/spectrums/201711*B_3.txt')

# import one file to get length of data points
scores =  numpy.loadtxt(files[0], delimiter='\t',  skiprows=5)
xvals=scores[:,0]
a = numpy.empty([scores.shape[0],len(files)])


# get the spectrum for each file and store in 'a' columns
for i, file in enumerate(files):
    scores =  numpy.loadtxt(file, delimiter='\t',  skiprows=5)
    a[:,i] = scores[:,1]

# plot
x=xvals[:-14] # missing x-axis (saved in xvals), keep in mind movingAv function reduces size of 
y=movingAv(a,15) # smooth with a 15 data point window
matplotlib.pyplot.plot(y)
