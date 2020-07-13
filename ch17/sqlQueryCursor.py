# sqlQueryCursor.py
# Purpose: Use a SQL query to select specific records.
# Usage: No script arguments needed.
import arcpy, traceback
fc = 'C:\Users\owner\Downloads\Sample_scripts\Lagos_GPS_GCPs.shp'

# Create the where_clause.
query = "Easting > 580000"
try:
    sc = arcpy.da.SearchCursor(fc, ['FID'], query)

    for row in sc:
        print(row[0])
    del(sc)
except:
    print('An error occurred.')
    traceback.print_exc()
    del(cursor)
