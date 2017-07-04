#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 19:55:10 2017

@author: dlicht
"""

import statistics as stat

n = 10
X = [10,9.8,8,7.8,7.7,7,6,5,4,2]
Y = [200,44,32,24,22,17,15,12,8,4]
#print(n,"\r",X,"\r",Y)

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

Pearson = numerator / ( n * Xsig * Ysig)

print("%.3f" % Pearson)