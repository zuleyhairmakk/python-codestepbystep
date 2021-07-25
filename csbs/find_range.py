# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def find_range(x):
    k = min(x)
    m = max(x)
    range = m - k
    if range == 0:
        return 1
    else:
        return (range+1)

    