# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def mirror(list1):
    list2=[]
    list2=list1.copy()
    list3= []
    list3= list2[::-1]
    list1.extend(list3)
    print(list1)


    