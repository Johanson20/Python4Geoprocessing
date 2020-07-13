#-------------------------------------------------------------------------------
# Name:        currency.py
# Purpose:     Converts between Euros and US Dollars
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
        print('Usage: number {currency (US or E)}\nExample: 100 US')
    elif numargs == 2:
        currency = float(sys.argv[1])
        altcurrency = 0.7 * currency
        print("Since you didn't specify a currency, I'm assuming US to Euros.")
        print("{} US Dollars is equivalent to {} Euros".format(currency, altcurrency))
    else:
        units = ['US', 'E']
        currency = float(sys.argv[1])
        unit = sys.argv[2]
        if unit.upper() == units[1]:
            print("{} Euros is equivalent to {} US Dollars".format(currency, round(currency/0.7, 2)))
        else:
            print("{} US Dollars is equivalent to {} Euros".format(currency, round(0.7*currency, 2)))

if __name__ == '__main__':
    main()
