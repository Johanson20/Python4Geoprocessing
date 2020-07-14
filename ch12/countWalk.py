#-------------------------------------------------------------------------------
# Name:        countWalk.py
# Purpose:     Walks through a folder and prints features classes and number
#              of rows in attribute table
#
# Author:      Johanson Onyegbula
#
# Created:     06/06/2020
#-------------------------------------------------------------------------------
import os, sys, arcpy

def main():
    indir = sys.argv[1]
    for directory, subdir, files in os.walk(indir):
        arcpy.env.workspace = directory
        for ff in files:
            f = os.path.join(directory, ff)
            if f.endswith('.shp'):
                rows = arcpy.GetCount_management(f)
                print('{} has {} entries'.format(f, int(rows[0])))

if __name__ == '__main__':
    main()
