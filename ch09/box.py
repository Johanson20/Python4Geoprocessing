#-------------------------------------------------------------------------------
# Name:        box.py
# Purpose:     Checks if coordinates of a point is within a unit box
#
# Author:      Johanson Onyegbula
#
# Created:     31/05/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

def main():
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    if 0 <= x <= 1 and 0 <= y <= 1:
        print('({},{}) is in the box.'.format(x,y))
    else:
        print('({},{}) is outside the box.'.format(x,y))

if __name__ == '__main__':
    main()
