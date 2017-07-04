#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:45:18 2017

@author: dlicht
"""

P = 1/3
insp = 5

ans = 0

#add up chance of first defect on 1st try, 2nd try.... 5th try
for n in range(1,insp+1):
    ans += (1-P)**(n-1) * P
    print(n, (1-P)**(n-1) * P, "cummulative: ",ans)

print(round(ans,3))