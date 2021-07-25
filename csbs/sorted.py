# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def sorted(a):
    s=0
    for i in range(0, len(a)-1):
        if a[i] < a[i+1]:
            s+=1
        else:
                break
                
    if s == (len(a)-1):
        return True
    else:
        return False


    