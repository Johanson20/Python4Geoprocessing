#-------------------------------------------------------------------------------
# Name:        reclassify
# Purpose:     Reclassifies cell values in a raster file into another set of
#              values, individually or in ranges
#
# Author:      Johanson Onyegbula
#
# Created:     24/05/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy

def main():
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = 'C:\Users\owner\Downloads\Sample_scripts\ch06'
    inRaster = 'C:\Users\owner\Downloads\Sample_scripts\ch06\bbn.tif'
    inField = 'Value'
    outRaster = arcpy.Reclassify_3d(inRaster, inField, )
    outRaster.save('koko.tif')
    del(outRaster)
    arcpy.env.overwriteOutput = False

if __name__ == '__main__':
    main()
