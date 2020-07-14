#-------------------------------------------------------------------------------
# Name:        segProc.py
# Purpose:     Calculates the Euclidean distance between two points
#
# Author:      Johanson Onyegbula
#
# Created:     11/06/2020
#-------------------------------------------------------------------------------
import math, sys

def perimeter(l1, l2, l3):
    '''Calculate the perimeter of a triangle'''
    peri = l1 + l2 + l3
    return peri

def triangleType(l1, l2, l3):
    '''Check what type of triangle it is'''
    if max(l1, l2, l3) == min(l1, l2, l3):
        triangle = 'Equilateral'
    elif l1 == l2 or l1 == l3 or l2 == l3:
        triangle = 'Isosceles'
    else:
        triangle = 'Neither equilateral nor isosceles'
    return triangle

def area(l1, l2, l3):
    '''Calculates the area of a triangle'''
    p = perimeter(l1, l2, l3)/2.0
    areaT = math.sqrt(p*(p-l1)*(p-l2)*(p-l3))
    return areaT

def main():
    side1 = float(sys.argv[1])
    side2 = float(sys.argv[2])
    side3 = float(sys.argv[3])

    print('Triangle sides: {}, {}, {}'.format(side1, side2, side3))
    print('Perimeter = {}\nType = {}\nArea = {}'.format(perimeter(side1, side2, side3),
    triangleType(side1, side2, side3), area(side1, side2, side3)))

if __name__ == '__main__':
    main()
