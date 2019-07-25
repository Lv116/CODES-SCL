#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:41:15 2019

@author: vyom
"""
def gamez():
    
    import random
    for x in range(1):
        x = random.randint(1,21)
        chance=0
        g=0
        print("Welcome to the number guessing Game(Only 3 changes allowed)")
        name=input("Hi, What is your Name?- ")
        print("Well,",name,"I have chosen a number between 1 and 20")
        if (g==x):
            chance += 1
            print("Good job.",name,"Your answer is correct and you guessed my no. in ", chance,"chances :)")
        
        while(g!=x and chance<3):
            print("Take a guess")
            g=int(input(""))
            if(g>x):
                print("Your guess is too high...")
                chance+=1
            elif(g<x):
                print("Your guess is too low...")
                chance+=1
            else:
                chance+=1
                print("Good job.",name,"Your answer is correct and you guessed my no. in ", chance,"chances :)")
        if (chance==3 and g!=x):
            print("You were unable to guess my number and lost all 3 chances... :/ The no. was-",x)
        replay()
        
def replay():
    print ("if you want to play again type '1' and if you want to leave type '0'")
    c=(input(""))
    if(c=='1'):
        print("LOADING.....")
        print("Restarting game....")
        gamez()
    elif(c=='0'):
        print("Bye, then.....")
    else:
        print("ERROR")
        replay()
gamez()   
