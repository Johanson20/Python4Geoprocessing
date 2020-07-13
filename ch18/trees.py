#-------------------------------------------------------------------------------
# Name:        trees.py
# Purpose:     Stores information about two fields in a dBase file
#              in a dictionary
# Usage:       Accepts three arguments - a full path dBase file and two fields
#
# Author:      Johanson Onyegbula
#
# Created:     19/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, arcpy

def main():
    infile = sys.argv[1]
    field1 = sys.argv[2]
    field2 = sys.argv[3]
    cursor = arcpy.da.SearchCursor(infile, [field1, field2])
    dBaseDict = {}
    for row in cursor:
        if not row[0] in dBaseDict.keys():
            dBaseDict[row[0]] = row[1]

    print('Tree dictionary:')
    print(dBaseDict)
    del(cursor)

if __name__ == '__main__':
    main()
