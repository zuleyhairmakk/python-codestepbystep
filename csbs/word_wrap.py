# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def word_wrap(x):
    with open(x, "r" ) as file :
        content = file.read().splitlines()
        for line in content:
            myfunc(line)
def myfunc(line):
    s = len(line)
    i=0
    j=60
    while s >= 60 :
        print(line[i:j])
        s-=60
        i+=60
        j+=60
    while 0 <= s< 60 :
        print(line[i:])
        break
                    



    