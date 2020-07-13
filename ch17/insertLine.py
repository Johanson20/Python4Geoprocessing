# insertLine.py
# Purpose: Find the centroids of two polygons in park.shp, then
#          create a line segment connecting these points
#          and add it to parkLines with left_fid set to 50.
# Solution is similar to the insertPolygon.py example

import arcpy, os, traceback

fcPoly = 'C:/Users/owner/Downloads/Sample_scripts/ch07/shapefiles/boundingBoxes.shp'
origfcLine = 'C:\Users\owner\Downloads\Sample_scripts\ch06\shapefiles\simpleLine.shp'
fcLine = 'C:\Users\owner\Downloads\Sample_scripts/' + os.path.basename(origfcLine)
arcpy.env.overwriteOutput = True
arcpy.Copy_management(origfcLine, fcLine)
try:
    #creates points
    sc = arcpy.da.SearchCursor(fcPoly, ['SHAPE@XY'])
    # Get 2 centroids
    row = sc.next()
    point1 = arcpy.Point(row[0][0], row[0][1])
    print('Point1: ({0},{1})'.format(row[0][0], row[0][1]))
    row = sc.next()
    point2 = arcpy.Point(row[0][0], row[0][1])
    print('Point2: ({0},{1})'.format(row[0][0], row[0][1]))
    del(sc)
except:
    print('An error occurred while creating points.')
    traceback.print_exc()
    del(sc)

try:
    #creates and inserts the line
    cursor = arcpy.da.InsertCursor(fcLine, ['Name', 'SHAPE@'])
    myArray = arcpy.Array([point1, point2])
    line = arcpy.Polyline(myArray)
    newLineArray = ['Testing ...', line]
    cursor.insertRow(newLineArray)
    print('New line inserted!')
    del(cursor)
except:
    print('An error in inserting line occurred.')
    traceback.print_exc()
    del(cursor)

### Create an array and then a polyline.  Then use an insert cursor.
