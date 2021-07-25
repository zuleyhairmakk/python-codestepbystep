# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""


    def remove_range(s,min,max):
    for i in range(min,max+1):
        if i in s:
            s.remove(i)