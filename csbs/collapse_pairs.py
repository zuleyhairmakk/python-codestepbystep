# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def collapse_pairs(num):
    for i in range(1, len(num),2):
        if (num[i-1]+num[i]) %2 == 0:
            num[i-1] = num[i-1]+num[i]
            num[i]= 0 
        else:
            num[i]=num[i-1]+num[i]
            num[i-1]=0



    