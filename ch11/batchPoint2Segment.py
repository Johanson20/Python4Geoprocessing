#-------------------------------------------------------------------------------
# Name:        batchPoint2Segment.py
# Purpose:     Converts line features to lines, then splits lines at vertices
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
    outspace = sys.argv[2]
    files = arcpy.ListFeatureClasses()

    for f in files:
        fh = arcpy.Describe(f)
        if fh.shapeType == 'Point':
            outline = os.path.splitext(f)[0] + 'Line.shp'
            outsplitline = os.path.splitext(f)[0] + 'Segment.shp'
            outline = os.path.join(inspace, outline)
            arcpy.PointsToLine_management(f, outline)
            print('{} created.'.format(outline))

            outfile = os.path.join(outspace, outsplitline)
            arcpy.SplitLine_management(outline, outfile)
            arcpy.Delete_management(outline)
            print('{} created.'.format(outfile))

if __name__ == '__main__':
    main()
