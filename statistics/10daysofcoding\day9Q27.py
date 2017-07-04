#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:30:09 2017

@author: dlicht
"""

#multiple linear regression
from sklearn import linear_model
x = [[0.18, 0.89], [1.0, 0.26], [0.92, 0.11], [0.07,0.37], [00.85,0.16],\
     [0.99,0.41],[0.87,0.47]]
y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.intercept_
b = lm.coef_
#print(a, b[0], b[1])

#use regression to make predictions on

Xpre = [[0.49,0.18],[0.57,0.83],[0.56,0.64],[0.76,0.18]]
#print(Xpre[0][0])

Ypre = []
for i in range(len(Xpre)):
    Ypre += [ a + b[0]*Xpre[i][0]+ b[1]*Xpre[i][1] ]
    
for y in Ypre: print("%.2f" % y)