#-------------------------------------------------------------------------------
# Name:        batchCount.py
# Purpose:     Counts the number of rows in point/polygon shapefiles
#
# Author:      Johanson Onyegbula
#
# Created:     05/06/2020
#-------------------------------------------------------------------------------
import sys, arcpy

def main():
    arcpy.env.workspace = sys.argv[1]
    substring = '*' + sys.argv[2] + '*'
    files = arcpy.ListFeatureClasses(substring)
    for f in files:
        file = arcpy.Describe(f)
        if file.shapeType == 'Point' or file.shapeType == 'Polygon':
            rows = arcpy.GetCount_management(f)
            print('{} has {} entries'.format(file.name, int(rows[0])))

if __name__ == '__main__':
    main()
