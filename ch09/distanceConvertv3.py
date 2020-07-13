#-------------------------------------------------------------------------------
# Name:        distanceConvertsv3.py
# Purpose:     Converts kilometers to miles and vice versa
#
# Author:      Johanson Onyegbula
#
# Created:     01/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

def main():
    numArgs = len(sys.argv)

    # If no user arguments are given, exit the script and warn the user.
    if numArgs == 1:
        print('Usage: numeric_distance {distance_unit (mi or km)}')
        print('Example: 5 km')
    # If only one user argument is given, set the unit to miles.
    elif numArgs < 3:
        unit = 'miles'
        dist = float(sys.argv[1])
        print('Warning: No distance unit provided. Assuming input is in miles.')
        print('{} miles is equivalent to {} kilometers'.format(dist, 1.6*dist))
    else:
        # Get the unit provided by the user
        unit = sys.argv[2]

        # Get the numeric distance (cast string to float).
        dist = float(sys.argv[1])

        # Perform conversion.
        mileList = ['mi', 'mi.', 'mile', 'miles']
        kmList = ['km', 'km.', 'kilometers', 'kilometer']

        if unit.lower() in mileList:
            output = dist*1.6
            print('{0} {1} is equivalent to {2} kilometers(s).'.format(dist, unit, output))
        elif unit.lower() in kmList:
            output = dist*.62
            print('{0} {1} is equivalent to {2} mile(s).'.format(dist, unit, output))
        else:
            print('Warning: unit must be either miles or kilometers')

if __name__ == '__main__':
    main()
