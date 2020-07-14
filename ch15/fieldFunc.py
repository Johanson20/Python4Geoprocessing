#-------------------------------------------------------------------------------
# Name:        fieldFunc.py
# Purpose:     Prints the name of the input file and fields in it
# Usage:       Takes an input file name and an output workspace
#
# Author:      Johanson Onyegbula
#
# Created:     11/06/2020
#-------------------------------------------------------------------------------
import arcpy, sys, os

arcpy.env.overwriteOutput = True
infile = sys.argv[1]
outputDir = sys.argv[2]

if not os.path.exists(outputDir):
    os.mkdir(outputDir)

def printFields(eg_file):
    '''Print the filename and fields in it'''
    fields = arcpy.ListFields(eg_file)
    print('Fields in {}:'.format(eg_file))
    for field in fields:
        print(field.name)

printFields(infile)
outfile = outputDir + '/' + os.path.basename(infile)
arcpy.CopyFeatures_management(infile, outfile)
print('{} copied to {}'.format(infile, outfile))
arcpy.AddField_management(outfile, 'AREA', 'FLOAT')
printFields(outfile)
