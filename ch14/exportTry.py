#-------------------------------------------------------------------------------
# Name:        exportTry.py
# Purpose:     Exports an ArcGIS format data file to a comma separated value file
# Usage:       Two arguments required: input file (shapefile) and output directory
#
# Author:      Johanson Onyegbula
#
# Created:     10/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, os, arcpy

def main():
    filename = sys.argv[1]
    outdir = sys.argv[2]
    arcpy.env.workspace = outdir
    arcpy.env.overwriteOutput = True
    basename = os.path.basename(filename)
    outfile = outdir + '/' + basename[:-4] + '.csv'
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    try:
        arcpy.QuickExport_interop(filename, outfile)
        print('Output created in: CSV, {}'.format(outdir))
    except arcpy.ExecuteError:
        print('Failed to execute(QuickExport).')
        print('Feature class {} is invalid.'.format(filename))

if __name__ == '__main__':
    main()
