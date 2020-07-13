#-------------------------------------------------------------------------------
# Name:        distribution
# Purpose:     Converts polygons to points by calculating their centroids, then
#              creates Thiessen polygons from these points
#
# Author:      Johanson Onyegbula
#
# Created:     24/05/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy

def main():
    arcpy.env.workspace = 'C:\Users\owner\Downloads\Sample_scripts\ch06'
    inputFeature = 'C:\Users\owner\Documents\Learning Materials\Johanson - 500 level\PROJECT\\adm&gaz\NGA_adm\NGA_adm1.shp'
    tempOut = 'Feat2Pt.shp'
    arcpy.FeatureToPoint_management(inputFeature, tempOut)
    arcpy.CreateThiessenPolygons_analysis(tempOut, 'voronoi.shp')

if __name__ == '__main__':
    main()
