# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:15:45 1998

@author: SCL1
"""

def calculator():
    a = eval(input('Enter First  number: '))
    b = eval(input('Enter Second number: '))
    op = input(''' 
 Enter the operator you want to use:
                          (+ for addition
                          - for subtraction
                          * for multiplication
                          / for division) 
                          ''')

    if (op == '+'):
        print( "=>" ,a , "+" , b)
        print(a + b)

    elif (op == '-'):
        print( "=>" ,a , "-" , b)
        print( a - b)

    elif (op == '*'):
        print( "=>" ,a , "*" , b)
        print(a * b)

    elif (op == '/'):
        print( "=>" ,a , "/" , b)
        print( round(a / b))

    else:
        print('Invalid operator...')
    retry()

def retry():
    A= input('''
Do you want to use the calculator again?
Please type 1 for YES or 0 for NO.
''')

    if (A == '1'):
        calculator()
    elif(A == '0'):
        print('Bye...')
    else:
        retry()
calculator()
