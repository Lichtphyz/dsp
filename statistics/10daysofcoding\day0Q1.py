# -*- coding: utf-8 -*-
"""
Spyder Editor

10 days of coding:  day 0, Q1

"""
n_in = '14'
N_in = '64630 11735 14216 99233 99233 99233 14470 4978 73429 38120 51135 67060 12345 12345'

#load data
n = n_in
n = int(n)
N = N_in
N = N.split(" ")
N = [float(num) for num in N]

#mean
mean = sum(N)/n
print(round(mean,1))

#median
N.sort()
middle = int(n/2)
if len(N)%2 == 0:
    medianlist = N[middle-1:-middle+1]
    median = sum(medianlist)/2
else:
    median = N[middle]
print(round(median,1))

#mode
N.sort()
freq = []
for num in N: freq += [N.count(num)]
print(freq)
mode_index = freq.index(max(freq))
mode = N[mode_index]
print(int(mode))