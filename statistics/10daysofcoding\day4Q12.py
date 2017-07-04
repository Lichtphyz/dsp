#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:10:25 2017

@author: dlicht
"""

def binomial(n,k):
    import math
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def Pn_boys(nboys,nchildren,Pboy):
    Pgirl = 1-Pboy
    ngirls = nchildren - nboys
    bicoef = binomial(nchildren,nboys)
    #print("binomial coef =",bicoef,"nboys = ",nboys)
    return bicoef*(Pboy**nboys)*(Pgirl**ngirls)

#loading data
##N = input()
N = "1.09 1"
N = N.split(" ")
N = [float(n) for n in N]

#calculate probabilities
Pboy = N[0]/(sum(N))
#print("Pboy = ",Pboy)
Pgirl = N[1]/(sum(N))

#add up probabilites for 3 to 6 of boys  [note: 2 or less girls would be more efficient]
P3plusboys = 0
for i in [6,5,4,3]:
    P3plusboys += Pn_boys(i,6,Pboy)
    #print(P3plusboys)
    
print(round(P3plusboys,3))