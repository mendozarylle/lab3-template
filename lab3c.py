#!/usr/bin/env python3

'''Lab 3 Inv 2 function operate '''

"""
Name: Lab3.py
Author: Rylle Mendoza 
Author ID: rmendoza10@myseneca.ca
Date: 2024/sept/25

Usage:

Description:
"""

def operate(number1, number2, operator):
    # Place logic in this function
    if operator == 'add':
        result = number1 + number2
    elif operator == 'subtract':
        result = number1 - number2
    elif operator == 'multiply':
        result = number1 * number2
    elif operator == 'divide':
        # Assuming you want to handle division as well
        if number2 != 0:
            result = number1 / number2
        else:
            result = 'Error: Division by zero is not allowed'
    else:
        result = 'Error: function operator can be "add", "subtract", or "multiply"'

    return result
    
if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))