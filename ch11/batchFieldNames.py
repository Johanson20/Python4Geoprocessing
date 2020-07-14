#-------------------------------------------------------------------------------
# Name:        batchFieldNames.py
# Purpose:     Lists all rasters in a given workspace and lists all field names
#              in each
#
# Author:      Johanson Onyegbula
#
# Created:     05/06/2020
#-------------------------------------------------------------------------------
import sys, arcpy

def main():
    arcpy.env.workspace = sys.argv[1]
    substring = '*' + sys.argv[2] + '*'
    files = arcpy.ListRasters(substring)
    for raster in files:
        print(raster)
        fields = arcpy.ListFields(raster)
        for field in fields:
            print('\t{}'.field(field))

if __name__ == '__main__':
    main()
