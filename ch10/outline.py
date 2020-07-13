#-------------------------------------------------------------------------------
# Name:        outLine
# Purpose:     Prints two nested lists using a for loop
#
# Author:      Johanson Onyegbula
#
# Created:     03/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    letters = ['a', 'b', 'c']
    for i in range(1,5):
        print('{}) Hehe'.format(i))
        for l in letters:
            print('\t{}) Hoho'.format(l))

if __name__ == '__main__':
    main()
