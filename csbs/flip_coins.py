# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def flip_coins(x):
    with open(x, "r") as file:
        content= file.readlines()
        for line in content:
            tur(line)
            
            
def tur(line):
    parts = line.split()
    h=0
    t=0
    for i in range(0, len(parts)):
        if 'h' in parts[i]:
            h+=1
        elif 't' in(parts[i]):
            t+=1
        elif 'H' in parts[i]:
            h+=1
        elif 'T' in parts[i]:
            t+=1
            
    s = h+t
    yd= round((h/s)*100)
    if yd>= 50 :
        print(f"{h} heads ({yd}%)")
        print("There were more heads!")
    else:
        print(f"{h} heads ({yd}%)")
    print()

                    



    