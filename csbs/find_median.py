# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def find_median(x):
    median = int (len(x) / 2)
    x.sort()
    return x [median]

    