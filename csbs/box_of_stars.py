# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def box_of_stars(x,y):
    for i in range(y):
        if(i==0 or i==y-1):
            print("*"*x)
        else:
                print("*"+ " "*(x-2)+ "*")
def main():
    box_of_stars(8,5)
                    



    