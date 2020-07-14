#-------------------------------------------------------------------------------
# Name:        erase
# Purpose:     This script erases the spatial extents of one shapefile from
#              another, like a subtraction of two shapefiles
#
# Author:      Johanson Onyegbula
#
# Created:     24/05/2020
#-------------------------------------------------------------------------------
import arcpy

def main():
    arcpy.env.workspace = 'C:\Users\owner\Downloads\Sample_scripts\ch06'
    inputFeature = 'C:\Users\owner\Documents\Learning Materials\Johanson - 500 level\PROJECT\\adm&gaz\NGA_adm\NGA_adm0.shp'
    eraseFeature = 'C:\Users\owner\Documents\Learning Materials\Johanson - 500 level\PROJECT\\adm&gaz\NGA_adm\Lagos_State.shp'
    outputFile = 'Naija_W_Lagos.shp'
    arcpy.Erase_analysis(inputFeature, eraseFeature, outputFile)

if __name__ == '__main__':
    main()
