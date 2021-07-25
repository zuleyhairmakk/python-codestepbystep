# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def second_half_letters(x):
    alph=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    x=x.lower()
    syc=0
    shl=0
    for i in range(len(x)):
        if(x[i] not in alph):
            syc +=1
        else:
            shl +=1
    return shl
        