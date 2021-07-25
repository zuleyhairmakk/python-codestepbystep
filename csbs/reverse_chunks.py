# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def reverse_chunks(a, x):
    res = ''
    i = 0
    while i + x <= len(a):
       slice = a[i:i+x]
       res += slice[::-1]
       i += x
    j = len(a) % x
    if j!= 0:
        res += a[-j:]
    return res