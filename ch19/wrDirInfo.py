#-------------------------------------------------------------------------------
# Name:        wrDirInfo.py
# Purpose:     Lists all files in a directory and writes their names, sizes
#              and data types to an output text file
# Usage:       Requires two arguments - a directory and a full path output text file
#
# Author:      Johanson Onyegbula
#
# Created:     22/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, os, arcpy

def main():
    inDir = sys.argv[1]
    outfile = sys.argv[2]
    arcpy.env.workspace = inDir
    try:
        files = os.listdir(inDir)
        with open(outfile, 'w') as outf:
            for infile in files:
                name = os.path.basename(infile)
                size = os.path.getsize(infile)
                desc = arcpy.Describe(infile)
                typ = desc.dataType
                toWrite = '{};{};{}\n'.format(name, size, typ)
                outf.write(toWrite)
    except WindowsError:
        print("{} doesn't exist or can't be found.".format(inDir))

if __name__ == '__main__':
    main()
