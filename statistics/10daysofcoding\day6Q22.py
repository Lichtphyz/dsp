#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 19:35:23 2017

@author: dlicht
"""

#load data
#Values = int(input())
#mu = int(input())
#sig = int(input())
#mp = float(input()) 
#z = float(input())

values = 100
mu = 500
sig = 80
mp = 0.95
z = 1.96

#mu_all = mu * values
#sig_all = sig * values**0.5

A = mu - z*sig/(values**0.5)
B = mu + z*sig/(values**0.5)

print("%.2f" % A)
print("%.2f" % B)