#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 06:15:22 2019

@author: vyom
"""

def HCF():
    
    A= int(input("Enter First number"))
    B= int(input("Enter second number"))
    
    if(A == B):
        print("The HCF of the two numbers is", A)
    
    while (A != B):
        
        if(A > B):
            A = A-B
       
        else:
            B = B-A
    
    print ("The HCF of the two numbers is",A)

HCF()
    