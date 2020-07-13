#-------------------------------------------------------------------------------
# Name:        timeTrig.py
# Purpose:     Calculates the time taken to compute the sine of cell values
#              in rasters
# Usage:       Takes two arguments - a full input directory or geodatabase of
#              rasters and an output directory
#
# Author:      Johanson Onyegbula
#
# Created:     12/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys
scriptPath = os.path.abspath(__file__)
scriptDir = os.path.dirname(scriptPath)
relPath = '../exerSupportCode'
reqPath = os.path.join(scriptDir, relPath)
sys.path.append(reqPath)

import timeReport, arcpy

def main():
    indir = sys.argv[1]
    outdir = sys.argv[2]
    arcpy.env.workspace = indir
    arcpy.env.overwriteOutput = True
    rasters = arcpy.ListRasters()
    arcpy.CheckOutExtension('Spatial')

    if not os.path.exists(outdir):
        os.mkdir(outdir)

    start = timeReport.getTime()
    for raster in rasters:
        outfil = os.path.splitext(raster)[0] + '.tif'
        outfile = os.path.join(outdir, outfil)
        outSin = arcpy.sa.Sin(raster)
        outSin.save(outfile)
        print('{} created.'.format(outfile))
    stop = timeReport.getTime()

    print(timeReport.reportDiffTime(start, stop, 'Calculating sine took'))

if __name__ == '__main__':
    main()
