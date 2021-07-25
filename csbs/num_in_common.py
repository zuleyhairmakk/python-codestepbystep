# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""


    def num_in_common(list1, list2):
    s = set()
    for item in list1:
        if item in list2:
            s.add(item)
    return len(s)