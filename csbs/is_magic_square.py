# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def is_magic_square(lst):

    sum1 = 0
    if len(lst) == 0:
        return True
    for row in lst:
        if len(row) != len(lst):
            return False
			
    
    for item in lst[0]:
        sum1 += item
		
	
   
	
    for i in range(len(lst)):
        sum2 = 0
        for row in lst:
            sum2 += row[i]
        if sum2 != sum1:
            return False
		
	
    sum2 = 0	
    for i in range(len(lst)):
        sum2 += lst[i][i]
    if sum2 != sum1 :
        return False
			
	
    sum2 = 0
    for i in range(len(lst)):
        sum2 += lst[i][-(i+1)]
    if sum2 != sum1:
        return False
			
    return True


    