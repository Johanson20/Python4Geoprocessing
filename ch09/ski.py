#-------------------------------------------------------------------------------
# Name:        ski.py
# Purpose:     Prints outs seasons pass fees for a ski resort for different
#              age ranges attending
#
# Author:      Johanson Onyegbula
#
# Created:     31/05/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

def main():
    age = float(sys.argv[1])
    if age <= 6:
        fee = 30
    elif 7 <= age <= 18:
        fee = 319
    elif 19 <= age <= 29:
        fee = 429
    else:
        fee = 549
    print('Season pass fee is ${}'.format(fee))

if __name__ == '__main__':
    main()
