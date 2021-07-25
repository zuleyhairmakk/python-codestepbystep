# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def switch_pairs(a):
    s=0
    x=1
    if len (a) % 2 !=0:
        while x < (len(a)-1):
            a.insert(s, a[x])
            a.pop(x+1)
            s+=2
            x+=2
    else:
        for i in range(1,len(a)+1 , 2):
            a.insert(s, a[i])
            a.pop(i+1)
            s+=2



    