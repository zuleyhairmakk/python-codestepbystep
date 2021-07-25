# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def split(a):
    newLi = []
    for i in range(0, len(a)):
        if a[i] % 2 == 0:
            k = int(a[i]/2)
            newLi.append(k)
            newLi.append(k)
        else:
            s = int(a[i]/2) + 1
            n = int (a[i]/2)
            newLi.append(s)
            newLi.append(n)
            
    return newLi
            

    