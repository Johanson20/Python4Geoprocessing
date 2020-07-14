#-------------------------------------------------------------------------------
# Name:        square
# Purpose:     Computes the square of cell values in a raster and stores in
#              another
#
# Author:      Johanson Onyegbula
#
# Created:     24/05/2020
#-------------------------------------------------------------------------------
import arcpy

def main():
    arcpy.env.workspace = 'C:\Users\owner\Downloads\Sample_scripts\ch06'
    inraster = arcpy.Raster('C:\Users\owner\Documents\Learning Materials\Johanson - 500 level\PROJECT\SPOT_Data_Lagos_Abuja\DEM01_Clip_SPOT_abuja_up.tif')
    outraster = arcpy.sa.Square(inraster)
    outraster.save('squareRaster.tif')

if __name__ == '__main__':
    main()
