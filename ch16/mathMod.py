#-------------------------------------------------------------------------------
# Name:        mathMod.py
# Purpose:     Creates various functions and tests them
#
# Author:      Johanson Onyegbula
#
# Created:     12/06/2020
#-------------------------------------------------------------------------------
import sys

def add(a, b):
    '''Return the addition of two numbers'''
    summ = a + b
    return summ

def sub(a, b):
    '''Return the difference of two numbers'''
    subtr = a - b
    return subtr

def mult(a, b):
    '''Return the product of two numbers'''
    multi = a*b
    return multi

if __name__=='__main__':
    A = float(sys.argv[1])
    B = float(sys.argv[2])
    sumV = add(A, B)
    product = mult(A, B)
    difference = sub(A, B)
    print(sumV, product, difference)
