#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 08:32:52 2019

@author: vyom
"""

def palindrome_check():
    a_1 = int(input("Enter the no. you want to check"))
    b = a_1
    a_2 = 0
    
    while(b>0):
        a_2 = a_2 * 10 + b%10
        b = b//10
        
    if(a_2 == a_1):
       
        print("The entered no. is a Palindrome")
    else:
        print("The entered no. isn't a Palindrome")
    retry()

def retry():
    i = input("Enter 'YES' if you want to check again and 'NO' if you don't want to... " )
    if (i=='YES'):
        palindrome_check()
    elif(i == 'NO'):
        print('Bye then.....')
    else:
        retry()
            
palindrome_check()        