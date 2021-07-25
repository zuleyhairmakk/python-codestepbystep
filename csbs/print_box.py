# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:39 2021

@author: züleyha
"""
def print_box(filename,width):

    with open(filename,'r') as file:

        print(width*"#")
        lines = file.readlines()
        lines =[ i.strip() for i in lines]
        lines =[ i.replace("_","") for i in lines]
            
        lines = [ i.capitalize() for i in lines]

        lines[:] = (elem[:width-2] for elem in lines)
    
        
        #print(lines)
        for i in range(len(lines)):
            length=int(len(lines[i]))
            if len(lines[i])==0:
                print("#"+(width-2)*' '+"#")
            else:
             
                print("#"+lines[i]+(width-length-2)*" "+"#")
       
        print(width*"#")
        

        #print("#"+(width-2)*' '+"#")
                    



    