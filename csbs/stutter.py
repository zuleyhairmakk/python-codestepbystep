# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def stutter(nums):
    i = 0
    while i < len(nums):
        nums.insert(i+1,nums[i])
        i+=2
    return nums
        
    


    