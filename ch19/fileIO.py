#-------------------------------------------------------------------------------
# Name:        fileIO.py
# Purpose:     Performs common file handling operations
#
# Author:      Johanson Onyegbula
#
# Created:     22/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    infile = open('C:\Users\owner\Downloads\Sample_scripts\ch19/test.txt', 'w')
    infile.write('365\nMonday\tTuesday\tWednesday\tThursday\tFriday\n')
    infile.write('1,2,3')
    infile.close()

    fh = open('C:\Users\owner\Downloads\Sample_scripts\ch19/test.txt', 'r')
    line1 = fh.readline()
    print(line1)
    line2 = fh.readline()
    dayList = line2.split('\t')
    for day in dayList:
        print(day)
    line3 = fh.readline()
    numList = (line3.split(','))
    numLi = [int(n) for n in numList]
    print('The sum is {}.'.format(sum(numLi)))
    fh.close()


if __name__ == '__main__':
    main()
