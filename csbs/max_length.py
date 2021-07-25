# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""


    def max_length(s):
    if len(s) == 0:
        return 0
    length = set()
    for item in s:
        length.add(len(item))
    return max(length)

