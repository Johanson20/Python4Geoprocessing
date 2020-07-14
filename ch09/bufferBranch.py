#-------------------------------------------------------------------------------
# Name:        bufferBranch.py
# Purpose:     Creates buffers around shapefiles only
#
# Author:      Johanson Onyegbula
#
# Created:     01/06/2020
#-------------------------------------------------------------------------------
import os, sys, arcpy

def main():
    file = sys.argv[1]
    desc = arcpy.Describe(file)
    arcpy.env.overwriteOutput = True
    if desc.dataType == 'ShapeFile':
        output = os.path.join(os.path.dirname(file), os.path.basename(file)[:-4] + 'Buffer.shp')
        numargs = len(sys.argv)
        if numargs == 1:
            print('Error: No file given')
        elif numargs == 2:
            arcpy.Buffer_analysis(file, output, '1 mile', 'OUTSIDE_ONLY', 'ROUND', 'ALL')
            print('No buffer distance given. Used default buffer distance of 1 mile')
            print('Buffer output', output)
        else:
            value = sys.argv[2]
            arcpy.Buffer_analysis(file, output, value, 'OUTSIDE_ONLY', 'ROUND', 'ALL')
            print('Buffer distance: ', value)
            print('Buffer output', output)
    else:
        print('Input data format must be shapefile.\nCould not buffer input file: {}'.format(file))

if __name__ == '__main__':
    main()
