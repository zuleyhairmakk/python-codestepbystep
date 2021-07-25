# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def find_range_2d(li1):
    if len(li1) ==0:
        return 0
    myList = []
    for i in li1:  
        
        for k in range(len(i)):
            myList.append(i[k])
    if max(myList) == min(myList):
        return 1
    rang = max(myList) - min(myList)
    return rang+1


    