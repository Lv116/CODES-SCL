#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 18:25:45 2019

@author: vyom
"""

def ISBN():
    cd = [10,16,1,11,5,6,9]
    n = input("Enter 10 digit ISBN code- ")
    if (len(n) != 10):
        print("ERROR....." ,
              "|||ISBN must be 10 digit :/")
        ISBN()
    s=(1*int(n[0])+2*int(n[1])+3*int(n[2])+4*int(n[3])+5*int(n[4])+6*int(n[5])+7*int(n[6])+8*int(n[7])+9*int(n[-2]))//11
    if(s in cd):
        print("The entered ISBN is correct... :)")
    else:
        print("Incorrect ISBN. Try Again.... :/")
        ISBN()
                
ISBN() 



