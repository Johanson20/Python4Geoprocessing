#-------------------------------------------------------------------------------
# Name:        avgNumbers.py
# Purpose:     Finds the mean of numbers in each line of a text file
#              and stores in another text file
# Usage:       Requires two arguments - a full path file name and an output directory
#
# Author:      Johanson Onyegbula
#
# Created:     23/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, os, numpy

def main():
    infile = sys.argv[1]
    outDir = sys.argv[2]
    basename = os.path.basename(infile)
    outfile = outDir + '/' + os.path.splitext(basename)[0] + '2.txt'
    try:
        with open(infile, 'r') as inf:
            with open(outfile, 'w') as outf:
                inf.readline()
                for line in inf:
                    values = [float(val) for val in line.split('\t')]
                    avg = numpy.mean(values)
                    outf.write('{}\n'.format(avg))
        print('{} created.'.format(outfile))
    except IOError:
        print("{} doesn't exist or can't be found.".format(infile))

if __name__ == '__main__':
    main()
