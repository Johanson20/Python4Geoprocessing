#-------------------------------------------------------------------------------
# Name:        radiusRaw.py
# Purpose:     Calculates radius of a circle
#
# Author:      Johanson Onyegbula
#
# Created:     01/07/2020
#-------------------------------------------------------------------------------
import sys, math

try:
    radius = float(sys.argv[1])
    area = math.pi*(radius**2)
except ValueError:
    print('''Radius must be numeric; {} is not numeric.
Default radius of 1 used.'''.format(sys.argv[1]))
    radius = 1.0
    area = math.pi*(radius**2)
print('Radius = {}\tArea = {}'.format(radius, area))
