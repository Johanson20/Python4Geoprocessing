#-------------------------------------------------------------------------------
# Name:        trails.py
# Purpose:     Calculates min and max of a numeric field
# Usage:       Accepts three arguments - a full path feature class, an
#              identifying field and a numeric field
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
    idfield = sys.argv[2]
    numfield = sys.argv[3]
    cursor = arcpy.da.SearchCursor(infile, [idfield, numfield])
    egDict = {}
    for row in cursor:
        egDict[row[0]] = row[1]
    del(cursor)

    mini = min(egDict.values())
    maxi = max(egDict.values())
    minkeys = []
    maxkeys = []
    for ind, val in egDict.items():
        if val == mini:
            minkeys.append(ind)
        elif val == maxi:
            maxkeys.append(ind)

    print('Minimum {0} = {1}\nFeature(s) with minimum {0}: {2}'.format(numfield, mini, minkeys))
    print('Maximum {0} = {1}\nFeature(s) with maximum {0}: {2}'.format(numfield, maxi, maxkeys))

if __name__ == '__main__':
    main()
