# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def vowel_count(sent):
    list=[0,0,0,0,0]
    for letter in sent:
        if letter == 'a':
            list[0]+=1
        elif letter =='e':
            list[1]+=1
        elif letter =='i':
            list[2]+=1
        elif letter =='o':
            list[3]+=1
        elif letter =='u':
            list[4]+=1
    return list


    