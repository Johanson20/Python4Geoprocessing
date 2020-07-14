#-------------------------------------------------------------------------------
# Name:        batchPostOffice.py
# Purpose:     Counts records in point and polygon features in a workspace
#
# Author:      Johanson Onyegbula
#
# Created:     05/06/2020
#-------------------------------------------------------------------------------
import arcpy, sys, os

def main():
    arcpy.env.workspace = sys.argv[1]
    outspace = sys.argv[2]
    files = arcpy.ListFeatureClasses('*data*')
    for f in files:
        if fh.shapeType == 'Point':
            out = os.path.basename(f)
            outf = os.path.splitext(out)[0] + 'Postal'
            infile = os.path.join(arcpy.env.workspace, f)
            outfile = os.path.join(outspace, outf)
            arcpy.CreateThiessenPolygons_analysis(infile, outfile)
            print('{} created.'.format(outfile))

if __name__ == '__main__':
    main()
