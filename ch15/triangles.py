#-------------------------------------------------------------------------------
# Name:        triangles.py
# Purpose:     Calculates values of geometric properties relating to triangles
#
# Author:      Johanson Onyegbula
#
# Created:     11/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math, sys

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

def segLength(x1, y1, x2, y2):
    '''Calculate the distance between two points'''
    sqrLine = (x1 - x2)**2 + (y1 - y2)**2
    dist = math.sqrt(sqrLine)
    return dist

print('Segment ({}, {}) to ({}, {}) has length: {:.2f}'.format(x1, y1, x2, y2, segLength(x1, y1, x2, y2)))
