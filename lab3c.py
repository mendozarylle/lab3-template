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
    if operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'  # Error for unrecognized operators

if __name__ == '__main__':
    print(operate(10, 20, 'add'))        # Expected output: 30
    print(operate(2, 3, 'add'))          # Expected output: 5
    print(operate(100, 5, 'subtract'))   # Expected output: 95
    print(operate(10, 20, 'subtract'))   # Expected output: -10
    print(operate(5, 5, 'multiply'))     # Expected output: 25
    print(operate(10, 100, 'multiply'))  # Expected output: 1000
    print(operate(100, 5, 'divide'))     # Expected output: Error message
    print(operate(100, 5, 'power'))      # Expected output: Error message