#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 05:20:40 2019

@author: vyom
"""

def Age():
    print("Type ages of students one by one in NUMERICAL value...")
    A=0
    B=0
    C=0
    D=0
    while True:
        a=input()
        if(a.isdigit()):
            n=int(a)
            if (n<12):
                D = D + 1
            elif(n<15):
                A = A + 1
            elif(n<17):
                B = B + 1
            else:
                C = C + 1
        else:
            break
        
        
    print("GROUP A: 12 yrs. and above but less than 15-",A,
          "n\GROUP B: 15 yrs. and above but less than 17-",B,
          "n\GROUP C: 17 yrs. and above but less than 19-",C,
          "n\GROUP D: Lesser than 12 yrs.-",D)
Age()