# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def word_count(x):
    a=x.split(" ")
    s=0
    for i in a:
        if(i==""):
            s +=1
    for i in range(s):
        a.remove("")
    return len(a)
    