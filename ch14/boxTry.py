#-------------------------------------------------------------------------------
# Name:        boxTry.py
# Purpose:     Find the minimum bounding rectangles for the features in each
#              shapefile in a folder
#
# Author:      Johanson Onyegbula
#
# Created:     10/06/2020
#-------------------------------------------------------------------------------
import sys, os, arcpy

def main():
    arcpy.env.workspace = 'C:\Users\owner\Downloads\Sample_scripts\ch06\shapefiles'
    arcpy.env.overwriteOutput = True
    features = arcpy.ListFeatureClasses()
    for feature in features:
        try:
            outfile = feature[:-4] + 'Bound.shp'
            arcpy.MinimumBoundingGeometry_management(feature, outfile)
            print('{} created'.format(outfile))
        except arcpy.ExecuteError:
            print(arcpy.GetMessage(2))
            print(arcpy.GetMessage(3))

if __name__ == '__main__':
    main()
