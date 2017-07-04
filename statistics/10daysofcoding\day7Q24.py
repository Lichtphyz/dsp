#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 19:55:10 2017

@author: dlicht
"""

n = 10
X = [10,9.8,8,7.8,7.7,1.7,6,5,1.4,2]
Y = [200,44,32,24,22,17,15,12,8,4]
#print(n,"\r",X,"\r",Y)

#enter data
#n = int(input())
#X = input()
#X = X.split(" ")
#print(X)
#X = [float(num) for num in X[0:-1]]
#Y = input()
#Y = Y.split(" ")
#print(X)
#Y = [float(num) for num in Y]

#create lists of ranks for X
Xranks=[]
for Ranked in X:
    count = 1
    for x in X:
        if x < Ranked: count += 1
    Xranks += [count]
print(Xranks)

#create lists of ranks for Y
Yranks=[]
for Ranked in Y:
    count = 1
    for y in Y:
        if y < Ranked: count += 1
    Yranks += [count]
print(Yranks)

summed = 0
#do the rank difference summation
for i in range(len(Xranks)):
    summed += ( Xranks[i]-Yranks[i] )**2
    print(summed)

Spearmans = 1 - 6 * summed / ( n *(n*n -1))

print("%.3f" % Spearmans)