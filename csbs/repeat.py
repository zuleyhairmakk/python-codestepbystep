# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def repeat(li1,k):
    newLi = li1.copy()
    if k <= 0:
        li1.clear()
    li1.clear()
    for i in newLi:
        for x in range(0,k):
            li1.append(i)
    print(li1)


    