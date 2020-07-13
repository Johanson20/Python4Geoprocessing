#-------------------------------------------------------------------------------
# Name:        sizeDict.py
# Purpose:     Prints out file names and file sizes in a directory
# Usage:       Accepts one argument - directory path
#
# Author:      Johanson Onyegbula
#
# Created:     19/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, os, numpy

def main():
    inDir = sys.argv[1]
    files = os.listdir(inDir)
    dictFiles = {}
    for file in files:
        infile = os.path.join(inDir, file)
        filesize = os.path.getsize(infile)
        dictFiles[infile] = filesize
    print(dictFiles)

    values = dictFiles.values()
    avg = numpy.mean(values)
    print('Average file size: {}'.format(avg))

if __name__ == '__main__':
    main()
