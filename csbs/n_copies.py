# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def  n_copies(li1):
    newLi = []
    for i in li1:
        if i <+ 0:
            continue
        else:
            for k in range(0, i):
                newLi.append(i)
    return newLi 
               

    