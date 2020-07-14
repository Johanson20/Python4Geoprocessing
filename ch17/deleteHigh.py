#-------------------------------------------------------------------------------
# Name:        deleteHigh.py
# Purpose:     Deletes rows with values of a field higher than a given value
# Usage:       Requires three arguments - an input path file name, a numeric
#              field and a search value
#
# Author:      Johanson Onyegbula
#
# Created:     19/06/2020
#-------------------------------------------------------------------------------
import sys, arcpy, traceback, os

def main():
    infile = sys.argv[1]
    field = sys.argv[2]
    value = sys.argv[3]
    arcpy.env.overwriteOutput = True
    inputFile = 'C:\Users\owner\Downloads\Sample_scripts/' + os.path.basename(infile)
    arcpy.CopyFeatures_management(infile, inputFile)

    try:
        whereClause = "{} > {}".format(field, value)
        cursor = arcpy.da.UpdateCursor(inputFile, field, whereClause)
        for row in cursor:
            cursor.deleteRow()
        print('Deletion complete!')
        del(cursor)
    except:
        print('An error in deleting fields occured!')
        traceback.print_exc()
        del(cursor)

if __name__ == '__main__':
    main()
