#-------------------------------------------------------------------------------
# Name:        rasterNames.py
# Purpose:     Prints jpg rasters in a semi-colon delimited list
# Usage:       An input workspace required
# Author:      Johanson Onyegbula
#
# Created:     05/06/2020
#-------------------------------------------------------------------------------
import arcpy, sys

def main():
    arcpy.env.workspace = sys.argv[1]
    jpgfiles = arcpy.ListRasters('*', 'JPG')
    ';'.join(jpgfiles)
    print(jpgfiles)

if __name__ == '__main__':
    main()
