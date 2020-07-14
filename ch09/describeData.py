#-------------------------------------------------------------------------------
# Name:        describeData.py
# Purpose:     Checks data type of argument and prints a property
#
# Author:      Johanson Onyegbula
#
# Created:     31/05/2020
#-------------------------------------------------------------------------------
import arcpy, sys

def main():
    file = sys.argv[1]
    desc = arcpy.Describe(file)

    if desc.dataType == 'ShapeFile': print(desc.shapeType)
    elif desc.dataType == 'RasterDataset': print(desc.format)
    else: print(desc.dataType)

if __name__ == '__main__':
    main()
