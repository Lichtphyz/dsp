#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 20:49:05 2017

@author: Daniel E. Licht
"""

my_list = [3, 4, 7, 2, 9, 170]

f = list(filter(lambda x: x%2 == 0, my_list))
print(f)

for n in f: print(n)


def fun(l):
    out = list(filter(lambda x: x%2 == 0, l))
    return out

#final answer:
f = lambda my_list: list(filter(lambda x: x%2 == 0, my_list)) 
for n in f(my_list): print(n)