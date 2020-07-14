#-------------------------------------------------------------------------------
# Name:        quickExport.py
# Purpose:     Converts feature classes to csv files
#
# Author:      Johanson Onyegbula
#
# Created:     05/06/2020
#-------------------------------------------------------------------------------
import arcpy, sys, os

def main():
    arcpy.env.overwriteOutput = True
    inspace = sys.argv[1]
    arcpy.env.workspace = inspace
    files = arcpy.ListFeatureClasses()

    for f in files:
        infile = os.path.join(arcpy.env.workspace, f)
        outf = os.path.splitext(f)[0] + '.csv'
        outfile = os.path.join(inspace, outf)
        arcpy.QuickExport_interop(infile, outfile)

    print('{} contains:'.format(inspace))
    print(arcpy.ListFiles('*csv'))

if __name__ == '__main__':
    main()
