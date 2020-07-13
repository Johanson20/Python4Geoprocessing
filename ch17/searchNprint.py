# searchNprint.py
# Purpose: Print each fire name in a file.
# Usage: No script arguments needed.
import arcpy, traceback
try:
    cursor = arcpy.da.SearchCursor('C:\Users\owner\Downloads\Sample_scripts\ch06\shapefiles\Lagos_GPS_GCPs.shp', ['FireName'])
    for row in cursor:
        print(row[0])
    del(cursor)
except:
    print('An error occurred')
    traceback.print_exc()
    del(cursor)
