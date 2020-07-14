#-------------------------------------------------------------------------------
# Name:        tableToDBASE.py
# Purpose:     Converts polygon features to lines
#
# Author:      Johanson Onyegbula
#
# Created:     05/06/2020
#-------------------------------------------------------------------------------
import arcpy, sys, os

def main():
    arcpy.env.overwriteOutput = True
    inspace = sys.argv[1]
    arcpy.env.workspace = inspace
    outspace = sys.argv[2]
    files = arcpy.ListTables()
    arcpy.TableToDBASE_conversion(files, outspace)

    print('{} contains:'.format(outspace))
    arcpy.env.workspace = outspace
    print(arcpy.ListTables('*', 'dBASE'))

if __name__ == '__main__':
    main()
