#-------------------------------------------------------------------------------
# Name:        deleteSpaceRows.py
# Purpose:     Deletes rows with spaces in its value
# Usage:       Requires two arguments - an input path file name, a text field
#
# Author:      Johanson Onyegbula
#
# Created:     19/06/2020
#-------------------------------------------------------------------------------
import sys, arcpy, traceback, os

def main():
    infile = sys.argv[1]
    field = sys.argv[2]
    arcpy.env.overwriteOutput = True
    inputFile = 'C:\Users\owner\Downloads\Sample_scripts/' + os.path.basename(infile)
    arcpy.CopyFeatures_management(infile, inputFile)

    try:
        whereClause = "{} LIKE '% %'".format(field)
        cursor = arcpy.da.UpdateCursor(inputFile, field, whereClause)
        for row in cursor:
            cursor.deleteRow()
            print('Removed row containing: {}'.format(row[0]))
        del(cursor)
    except:
        print('An error in deleting fields occured!')
        traceback.print_exc()
        del(cursor)

if __name__ == '__main__':
    main()
