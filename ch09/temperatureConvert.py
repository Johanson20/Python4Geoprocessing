#-------------------------------------------------------------------------------
# Name:        temperatureConvert.py
# Purpose:     Converts temperatures from Celsuis to Fahrenheit and vice versa
#
# Author:      Johanson Onyegbula
#
# Created:     01/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

def main():
    numargs = len(sys.argv)
    if numargs == 1:
        print('Usage: number {unit (C or F)}\nExample: 32 F')
    elif numargs == 2:
        temp1 = float(sys.argv[1])
        temp2 = 0.56 * (temp1 - 32)
        print("Since you didn't specify a scale, I'm assuming F to C.")
        print("{} degree(s) Fahrenheit is equivalent to {} degree(s) Celsius".format(temp1, temp2))
    else:
        units = ['F', 'C']
        temp = float(sys.argv[1])
        unit = sys.argv[2]
        if unit.upper() == units[1]:
            print("{} degree(s) Celsius is equivalent to {} degree(s) Fahrenheit".format(temp, round(1.8*temp + 32, 2)))
        else:
            print("{} degree(s) Fahrenheit is equivalent to {} degree(s) Celsius".format(temp, round(0.56*(temp - 32), 2)))

if __name__ == '__main__':
    main()
