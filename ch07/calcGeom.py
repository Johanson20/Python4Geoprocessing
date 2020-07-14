#-------------------------------------------------------------------------------
# Name:        calcGeom
# Purpose:     Creates a new field in the attribute table of a shapefile and
#              populates it with a geometrical property (area) of each feature
#
# Author:      Johanson Onyegbula
#
# Created:     24/05/2020
#-------------------------------------------------------------------------------
import arcpy, sys

def main():
    inputFeature = sys.argv[1]
    fieldName = sys.argv[2]
    geometry = sys.argv[3]
    unit = sys.argv[4]
    codeBlock = '!shape.' + geometry + '@' + unit + '!'

    arcpy.AddField_management(inputFeature, fieldName, 'float')
    arcpy.CalculateField_management(inputFeature, fieldName, codeBlock, 'PYTHON')

if __name__ == '__main__':
    main()
