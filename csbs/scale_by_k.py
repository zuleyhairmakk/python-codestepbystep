# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def scale_by_k(k):
    m = k.copy()
    for i in k:
        if i <= 0:
            k.pop(i)
    k.clear()
    for i in m:
        for x in range(0,i):
            k.append(i)
    print(k)
            

    