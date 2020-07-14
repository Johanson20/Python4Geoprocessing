#-------------------------------------------------------------------------------
# Name:        getCount
# Purpose:     Computes the number of polygons in a shapefile
#
# Author:      Johanson Onyegbula
#
# Created:     24/05/2020
#-------------------------------------------------------------------------------
import arcpy

def main():
    inputFeature = 'C:\Users\owner\Documents\Learning Materials\Johanson - 500 level\PROJECT\\adm&gaz\NGA_adm\NGA_adm2.shp'
    count = arcpy. arcpy.GetCount_management(inputFeature)
    print('There are {} polygons in {}'.format(count, inputFeature))

if __name__ == '__main__':
    main()
