#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 11:01:00 2017

@author: dlicht

10 days of coding:  day 0, Q3
"""

#create median function
def median(N):
    N.sort()
    middle = int(len(N)/2)
    if len(N)%2 == 0:
        medianlist = N[middle-1:-middle+1]
        median = sum(medianlist)/2
    else:
        median = N[middle]
    return median

#load data
n_in = '14'
N_in = '64630 11735 14216 99233 99233 56678 14470 4978 73429 38120 51135 67060 12345 12345'

#load data
n = n_in
n = int(n)
N = N_in
N = N.split(" ")
N = [float(num) for num in N]

#sort data by value
N.sort()
#split data into 2 halves, if there are an odd number of data points, disgard middle
middle = int(len(N)/2)
print('middle index = ',middle)
if len(N)%2 == 0:
    lowerhalf = N[:middle]
    upperhalf = N[middle:]
else:
    lowerhalf = N[:middle]
    upperhalf = N[middle+1:]
print('lower',lowerhalf)
print('upper',upperhalf)

#print interquartiles (Q1,Q2,Q3) as integers
print(int(median(lowerhalf)))
print(int(median(N)))
print(int(median(upperhalf)))