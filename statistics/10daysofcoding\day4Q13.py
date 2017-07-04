#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:10:25 2017

@author: dlicht
"""

def binomialC(n,k):
    import math
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def binomial(P,n,k):
    return binomialC(n,k) * P**k * (1-P)**(n-k)

#loading data
##N = input()
N = "12 10"
N = N.split(" ")
N = [int(n) for n in N]

P_rej = N[0]/100   #rejection probability
n_batch = N[1]    #size of piston batch
n_rej = 2         #critical number of rejects

print(P_rej,n_batch,n_rej)

#add up probabilites
P2orLess = 0
for i in range(n_rej+1):
    P2orLess += binomial(P_rej,n_batch,i)
    print("n rejects = ",i)
    print(binomial(P_rej,n_batch,i), P2orLess)
    
print(round(P2orLess,3))
#now print odds of more than n_rej
print(round(1-P2orLess,3))
