# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def collapse_spaces(x):
    with open(x, "r") as file:
        content = file.readlines()
        for line in content:
            tur(line)
            
def tur(line):
    parts = line.split()
    for i in range(0, len(parts)):
        print(parts[i] , end=" ")
    print()
                
                    



    