#-------------------------------------------------------------------------------
# Name:        freq.py
# Purpose:     Analyzes frequency of distinct entries in a particular field of
#              an attribute table
#
# Author:      Johanson Onyegbula
#
# Created:     24/05/2020
#-------------------------------------------------------------------------------
import arcpy

def main():
    arcpy.env.workspace = 'C:\Users\owner\Downloads\Sample_scripts\ch06'
    inputTable = 'Lagos_GPS_GCPs.shp'
    outputTable = 'C:\Users\owner\Downloads\Sample_scripts\ch06\Orders.dbf'
    freqField = 'Control_Or'
    #summaryField = ['1st Order', '2nd Order']
    arcpy.Frequency_analysis(inputTable, outputTable, freqField)

if __name__ == '__main__':
    main()
