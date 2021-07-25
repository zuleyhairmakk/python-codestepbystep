# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def input_stats(x):
    with open(x , "r") as file:
        content = file.read().splitlines()
        s = 0
        c = len(content)
        v=1
        mylist = []
        for i in range(len(content)):
            a = str(content[i])
            m= len(a)
            print(f"Line {v} has {m} chars")
            s+=m
            v+=1
            mylist.append(m)
        print(f"{c} lines; longest = {max(mylist)}, average = {s/c}")


                    



    