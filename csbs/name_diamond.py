# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def name_diamond(a):
    for i in range(len(a)):
        print(a[0:i])
    for i in range(len(a)):
        print((" " * i) + a[i:])
