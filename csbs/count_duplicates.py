# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def count_duplicates(lst):
    set = []
    dup = 0
    for i in lst:
        if i in set:
            dup += 1
        else:
            set.append( i )
    return dup


    