#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 21:41:27 2017

@author: dlicht
"""

import re

#print(re.split(r'\s*', 'here are some words'))
#words = re.split(r'\s*', 'here are some words')
#
#
#print(re.split(r'(\s*)', 'here are some words'))
#
#print(re.split(r'(s*)', 'here are some words'))
#
#print(re.split(r's*', 'here are some words'))
#
#print(re.split(r'[a-f]', 'askhg;akhglahljnkjh;ka;jkDHAGHFKAKDFDSADFSAF'))
#
#print(re.split(r'[a-fA-F0-4]', 'askhg;akhglahljnkjh;ka;jkDHAGHFKAKDFDSADFSAF',re.I|re.M))
#
#print(re.split(r'[a-f][a-f]', 'askhg;akhglabhljnkjh;kab;jkDHAGHFKAKDFDSADFSAF'))
#
#
#print (re.findall(r'\d','dahgkflkaflk324 main st.adaflkekd'))
#
#print (re.findall(r'\D','dahgkflkaflk324 main st.adaflkekd'))

print (re.findall(r'\d{1,5}','dahgkflkaflk324 main st.adaflkekd'))

print (re.findall(r'\d{1,5}\s\w+','dahgkflkaflk324 main st.adaflkekd'))

print (re.findall(r'\d{1,5}\s\w+\s\w+\.','dahgkflkaflk324 main st.adaflkekd'))


