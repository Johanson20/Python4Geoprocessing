#-------------------------------------------------------------------------------
# Name:        typeDict.py
# Purpose:     Stores file names and types in a dictionary
# Usage:       Accepts one argument - directory path
#
# Author:      Johanson Onyegbula
#
# Created:     19/06/2020
#-------------------------------------------------------------------------------
import sys, os, arcpy

def main():
    inDir = sys.argv[1]
    files = os.listdir(inDir)
    dictFiles = {}
    for fil in files:
        infile = os.path.join(inDir, fil)
        desc = arcpy.Describe(infile)
        typ = desc.datatype
        if typ in dictFiles.keys():
            dictFiles[typ].append(fil)
        else:
            dictFiles[typ] =[fil]

    print('Type dictionary:')
    print(dictFiles)

if __name__ == '__main__':
    main()
