#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 17:18:21 2017

@author: dlicht
"""

'''
Sample input:
6
6 12 8 10 20 16
5 4 3 2 1 5
'''    

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
n = input()
n = int(n)
X = input()
X = X.split(" ")
X = [float(num) for num in X]
F = input()
F = F.split(" ")
F = [int(num) for num in F]

#Use X and F to build whole data set to use with code from Q3
N = []
for i in range(len(X)):  N += [ X[i] ] * F[i]

#sort data by value
N.sort()
#split data into 2 halves, if there are an odd number of data points, disgard middle
middle = int(len(N)/2)
if len(N)%2 == 0:
    lowerhalf = N[:middle]
    upperhalf = N[middle:]
else:
    lowerhalf = N[:middle]
    upperhalf = N[middle+1:]

#calculate interquartiles (Q1,Q3)
Q1 = median(lowerhalf)
Q3 = median(upperhalf)

#print out Interquartile range (rounded to nearest 0.1)
print(round(Q3-Q1,1))
