# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""


    def max_occurrences(L):
    m={}

    for i in L:
        if i in m:
            m[i]=m[i]+1
        else:
            m[i]=1

    max_times=0
    for i in m:
        if (m[i]>max_times):
             max_times=m[i]
    return max_times
