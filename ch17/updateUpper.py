#-------------------------------------------------------------------------------
# Name:        updateUpper.py
# Purpose:     Updates a string type field in a shapefile to be all uppercase
# Usage:       Requires two arguments - an input path file name
#              and string type field
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
        cursor = arcpy.da.UpdateCursor(inputFile, field)
        for row in cursor:
            row[0] = row[0].upper()
            cursor.updateRow(row)
        print('{} created with uppercase values in {}.'.format(inputFile, field))
        del(cursor)
    except:
        print('An error in updating fields occured!')
        traceback.print_exc()
        del(cursor)

if __name__ == '__main__':
    main()
