#-------------------------------------------------------------------------------
# Name:        batchSimplifyPoly.py
# Purpose:     Simplifies all polygon feature classes in a workspace
#
# Author:      Johanson Onyegbula
#
# Created:     05/06/2020
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
            out = os.path.basename(f)
            outf = os.path.splitext(out)[0] + 'Simp'
            infile = os.path.join(arcpy.env.workspace, f)
            outfile = os.path.join(outspace, outf)
            arcpy.cartography.SimplifyPolygon(infile, outfile, 'POINT_REMOVE', 50)
            print('{} created.'.format(outfile))

if __name__ == '__main__':
    main()
