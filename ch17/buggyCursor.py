# buggyCursor.py
# WARNING: This script contains BUGS!  Remove them if you can.
# Purpose:   Count the number of records in park.shp with 'COVER'
#           field value that is neither 'woods' and nor 'orch'
# Usage: No arguments needed.

#arcpy not imported initially
import traceback, arcpy

filename = 'C:\Users\owner\Downloads\Sample_scripts\ch06\shapefiles\Lagos_GPS_GCPs.shp'
fields = ['Control_Or', 'FID']

count = 0  # Initialize count to zero.

try:
    #variable name is case sensitive
    cursor = arcpy.da.SearchCursor(filename, fields)    #cursor variable properly assigned
    for row in cursor:
        order = row[0]      #cover has index of 0 as it comes first in fields variable
        if order not in ['1st Order', '2nd Order']:
            count = count + 1
    del(cursor)     #cursor deletion must be outside for loop
    print('Number of records with very low order: {}'.format(count))
except:
    print('An error occurred.')
    traceback.print_exc()
    del(cursor)
