# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
import random

def flip_coin_three_heads():
    sonuc=""
    while("H H H" not in sonuc):
        k = random.randint(0,1)
        if(k == 1):
            sonuc +="T "
        else:
            sonuc +="H "
            
    print(str(sonuc))
    print("Three heads in a row!")
        
                    



    