# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def hours(x = input()):
    with open (x, "r") as file:
        content =file.readlines()
        print(f"Input file? {x}")
        for line in content :
            process_employee(line),
            
def process_employee(line):
    parts=line.split()
    userid =parts[0]
    name=parts[1]
    tot = 0
    count = 0
    for i in range (2, len(parts)):
        tot+= float(parts[i])
        count+=1
        
    average=round(tot/count, 1)
    print(name+" (ID#"+str(userid)+") worked "+ str(round(tot , 1))+" hours" +" ("+str(average)+"/day)")







                    



    