#-------------------------------------------------------------------------------
# Name:        split
# Purpose:     Splits a larger shapefile into subsets based on another shapefile
#              already segregated into parts with respect to some text-based
#              field's value (ArcMap-compatible text characters only in field)
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
    inputFeature = 'C:\Users\owner\Documents\Learning Materials\Johanson - 500 level\PROJECT\\adm&gaz\NGA_adm\NGA_adm0.shp'
    splitFeature = 'C:\Users\owner\Documents\Learning Materials\Johanson - 500 level\PROJECT\\adm&gaz\NGA_adm\NGA_adm2.shp'
    splitField = 'NAME_1'
    outputWorkspace = 'C:\Users\owner\Downloads\Sample_scripts\ch06'
    arcpy.Split_analysis(inputFeature, splitFeature, splitField, outputWorkspace)

if __name__ == '__main__':
    main()
