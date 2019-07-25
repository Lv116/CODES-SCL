#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 00:12:40 2019

@author: vyom
"""

def Denomination():
    n= int(input("Enter the amount you want to denominate"))
    
    print("No. of Rs.1000 notes required=",n//1000,
          "\nNo.of Rs.500 notes required=",(n%1000)//500,
          "\nNo. of Rs.100 notes required=",((n%1000)%500)//100,
          "\nNo. of Rs.50 notes required=",(((n%1000)%500)%100)//50,
          "\nNo. of Rs.10 notes required=",((((n%1000)%500)%100)%50)//10,
          "\nNo. of Rs.5 notes required=",(((((n%1000)%500)%100)%50)%10)//5,
          "\nNo. of Rs.2 notes required=",((((((n%1000)%500)%100)%50)%10)%5)//2,
          "\nNo. of Rs.1 notes required=",(((((((n%1000)%500)%100)%50)%10)%5)%2)//1)
    
Denomination() 
    
