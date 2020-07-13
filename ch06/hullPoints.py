#-------------------------------------------------------------------------------
# Name:        hullPoints
# Purpose:     Computes the minimum bounding polygon (usually a rectangle) of
#              any polygon and creates a point shapefile from its vertices
#Usage:        Requires full path to polygon shapefile as argument
# Author:      Johanson Onyegbula
#
# Created:     24/05/2020
#-------------------------------------------------------------------------------
import arcpy, sys, os

def main():
    arcpy.env.overwriteOutput = True
    inputFeature = sys.argv[1]
    arcpy.env.workspace = os.path.dirname(inputFeature)
    tempOut = 'boundingPoly.shp'
    arcpy.MinimumBoundingGeometry_management(inputFeature, 'boundingPoly.shp')
    arcpy.FeatureVerticesToPoints_management(tempOut, 'outerPoints.shp')

if __name__ == '__main__':
    main()
