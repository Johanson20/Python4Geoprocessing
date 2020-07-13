#-------------------------------------------------------------------------------
# Name:        bufferArgs.py
# Purpose:     Creates a buffer about a feature
# Usage:       Takes two arguments - an full path input file and a number
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
reqPath = os.path.join(scriptDir, 'exerSupportCode')
sys.path.append(reqPath)

import argHandler, arcpy

def main():
    infile = sys.argv[1]
    bufferDist = sys.argv[2]
    arcpy.env.workspace = os.path.dirname(infile)
    arcpy.env.overwriteOutput = True

    if argHandler.isShapefile(sys.argv, 1) and argHandler.getFloatArg(sys.argv, 2):
        arcpy.Buffer_analysis(os.path.basename(infile), 'buffOut.shp', bufferDist)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
