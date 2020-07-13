#-------------------------------------------------------------------------------
# Name:        rasterNames.py
# Purpose:     Prints jpg rasters in a semi-colon delimited list
#
# Author:      Johanson Onyegbula
#
# Created:     05/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy, sys

def main():
    workspace = sys.argv[1]
    jpgfiles = arcpy.ListRasters('*', 'JP2')
    ';'.join(jpgfiles)
    print(jpgfiles)

if __name__ == '__main__':
    main()
