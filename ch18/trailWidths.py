#-------------------------------------------------------------------------------
# Name:        trailWidths.py
# Purpose:     Calculates the average of a numeric field for each classification
#              of a classification field
# Usage:       Accepts three arguments - a full path feature class name, a
#              classification field and a numeric field
#
# Author:      Johanson Onyegbula
#
# Created:     19/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, arcpy, numpy

def main():
    infile = sys.argv[1]
    classfield = sys.argv[2]
    numfield = sys.argv[3]
    cursor = arcpy.da.SearchCursor(infile, [classfield, numfield])
    classDict = {}
    for row in cursor:
        if not row[0] in classDict.keys():
            classDict[row[0]] = [row[1]]
        else:
            classDict[row[0]].append(row[1])
    del(cursor)

    for ind in classDict.keys():
        avg = numpy.mean(classDict[ind])
        print('Classification: average {}: {:.2f}'.format(ind, avg))

if __name__ == '__main__':
    main()
