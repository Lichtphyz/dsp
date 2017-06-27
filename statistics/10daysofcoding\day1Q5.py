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
'''    

#import statistics as stat #for the EASY way

n = input()
n = int(n)
X = input()
X = X.split(" ")
X = [float(num) for num in X]

#print(round(stat.pstdev(X),1))   # . <-- Easy solution

#doing the math myself:
avg = sum(X)/n

sqr_dif = []
for x in X:  sqr_dif += [(x-avg)**2]

var = sum(sqr_dif)/n

square_root = var**0.5

print(round(square_root,1))