#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:15:56 2017

@author: dlicht

input format, all strings:
95 85
85 95
80 70
70 65
60 70

"""

import statistics as stat

#import and format data into two vectors X and Y
points = []
for i in range(5): points += [input().split(" ")]
#print(points)

X = []
Y = []
for i in range(len(points)):
    X += [int(points[i][0])]
    Y += [int(points[i][1])]

#print("X = ",X,"Y = ",Y)


#calculate the pearson correlation coefficient

#find averages
muX = stat.mean(X)
muY = stat.mean(Y)
#print(muX,muY)

#do the summation
numerator = 0
for i in range(len(X)):
    numerator += (X[i]-muX)*(Y[i]-muY)
    #print(numerator)

#calculate (population!) standard deviations
Xsig = stat.pstdev(X)
Ysig = stat.pstdev(Y)

Pearson = numerator / ( len(X) * Xsig * Ysig)
#print("%.3f" % Pearson)


#Linear Regression to find slope(b) and y-intercept(a)
b = Pearson * Ysig/Xsig
a = muY - b*muX


#a student scores an X value of 80, what is their expected Y value?
dx = 80
dy = b*dx
answer = dy + a

print("%.3f" % answer)