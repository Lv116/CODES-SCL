# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:56:11 2019

@author: SCL1
"""

n=int(input("enter:"))
count=0
for i in range(n):
    i+=1
    for j in range (1):
        print(" "*(n-1),end=(" "))
    print(chr(ord("A")+count))
    count+=1
    n-=1
    print()    
    