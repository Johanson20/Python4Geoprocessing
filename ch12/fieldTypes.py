#-------------------------------------------------------------------------------
# Name:        fieldTypes.py
# Purpose:     Prints all field names given a shapefile with attribute table
#
# Author:      Johanson Onyegbula
#
# Created:     06/06/2020
#-------------------------------------------------------------------------------
import sys, arcpy

def main():
    infile = sys.argv[1]
    fields = arcpy.ListFields(infile)
    listfield = []
    for field in fields:
        listfield.append(field.name)
    print(listfield)

if __name__ == '__main__':
    main()
