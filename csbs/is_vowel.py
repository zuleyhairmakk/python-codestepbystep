# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def is_vowel(x):
    vowel = ["a","e","i", "o","u"]
    x= x.lower()
    if x in vowel :
        return True
    else:
        return False
