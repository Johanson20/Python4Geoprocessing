#-------------------------------------------------------------------------------
# Name:        batchPoly2Line.py
# Purpose:     Converts polygon features to lines
#
# Author:      Johanson Onyegbula
#
# Created:     05/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy, sys, os

def main():
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = sys.argv[1]
    outspace = sys.argv[2]
    files = arcpy.ListFeatureClasses()

    for f in files:
        fh = arcpy.Describe(f)
        if fh.shapeType == 'Polygon':
            outf = os.path.splitext(f)[0] + 'Lines'
            infile = os.path.join(arcpy.env.workspace, f)
            outfile = os.path.join(outspace, outf)
            arcpy.PolygonToLine_management(infile, outfile)
            print('{} created.'.format(outfile))

if __name__ == '__main__':
    main()
