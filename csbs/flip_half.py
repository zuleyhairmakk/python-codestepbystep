# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def flip_half(List):
    temp=List[1::2]
    temp.reverse()
    for i in range(1,len(List),2):
        List[i]=temp[int(i/2)]


    