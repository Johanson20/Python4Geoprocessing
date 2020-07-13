# insertPoint.py
# Purpose: Insert a point with a Geometry object.
# Usage: Full path of file to copy and modify.
# Example input: C:/gispy/data/ch17/fires.shp

import arcpy, os, traceback, sys

fcOrig = sys.argv[1]
arcpy.env.overwriteOutput = True
fc = 'C:\Users\owner\Downloads\Sample_scripts/' + os.path.basename(fcOrig)
arcpy.Copy_management(fcOrig, fc)

try:
    ic = arcpy.da.InsertCursor(fc, ['FID', 'SHAPE@XY'])

    # Create a point with x = -70.1 and y = 42.07 to be used for the Shape field.
    myPoint = arcpy.Point(500000.1, 700000.07)

    # Create a row list with FireId=500000 and the new point
    newRow = [500000, myPoint]

    # Insert the new row.
    ic.insertRow(newRow)
    print('New row inserted.')

    del(ic)
except:
    print('An error occurred.')
    traceback.print_exc()
    del(ic)
