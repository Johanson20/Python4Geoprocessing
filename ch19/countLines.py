#-------------------------------------------------------------------------------
# Name:        countLines.py
# Purpose:     Counts and prints the number of lines in an input file if it exists
# Usage:       Requires one argument - a full path input text file
#
# Author:      Johanson Onyegbula
#
# Created:     22/06/2020
#-------------------------------------------------------------------------------
import sys

def main():
    infile = sys.argv[1]
    try:
        fh = open(infile, 'r')
        n = 0
        for line in fh:
            n = n + 1
        print('{} has {} lines.'.format(infile, n))
    except IOError:
        print("{} doesn't exist or can't be opened.".format(infile))

if __name__ == '__main__':
    main()
