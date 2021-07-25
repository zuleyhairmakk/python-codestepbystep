# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def three_consecutive(x, y, z):
    a = [x, y, z]
    a.sort()
    if a[1] == a[0] + 1 and a[2] == a[1] + 1:
        return True
    return False




    