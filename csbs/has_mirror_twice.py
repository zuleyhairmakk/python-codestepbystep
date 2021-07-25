# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def has_mirror_twice(a1,a2):
    lmd=len(a2)-1
    s=[a2[lmd-i] for i in range(lmd+1)]
    numOcc=[]
    counter=0
    if len(a2) ==1:
        for i in range(len(a1)):
            if a2[0] == a1[i]:
                counter+=1
        if counter >=2:
            return True
    for i in range(len(a1)):
        for j in range(len(s)):
            if (i+j) >=len(a1):
                break
            if s[j]==a1[i+j]:
                counter+=1
            else:
                counter=0
            if counter == len(s):
                numOcc.append(i)
    if len(numOcc)>=2:
        return True
    else:
        return False


    