#-------------------------------------------------------------------------------
# Name:        shape2kml
# Purpose:     Converts a shapefile to KML file at a given scale
#
# Author:      Johanson Onyegbula
#
# Created:     24/05/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy, sys

def main():
    workspace = sys.argv[1]
    inputFeature = sys.argv[2]
    kmlFeature = sys.argv[3]
    scale = sys.argv[4]
    tempLyr = 'tempLyr.lyr'

    featureLyr = arcpy.MakeFeatureLayer_management(inputFeature, tempLyr)
    print('Temporary layer {} created'.format(tempLyr))
    arcpy.LayerToKML_conversion(tempLyr, kmlFeature, scale)
    print('{} created'.format(kmlFeature))

if __name__ == '__main__':
    main()
