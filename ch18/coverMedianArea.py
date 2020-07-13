# coverMedianArea.py
# Purpose: Find the median area of polygons of each cover type.
# Usage: No arguments needed.
import arcpy, numpy

arcpy.env.workspace = 'C:\Users\owner\Downloads\Sample_scripts\ch06\shapefiles'
fc = 'Lagos_GPS_GCPs.shp'

# Populate the dictionary,
# accumulate a list of areas for each cover type.
d = {}
sc = arcpy.da.SearchCursor(fc, ['Control_Or', 'Easting'])
for row in sc:
    cover = row[0]
    area = row[1]
    if cover in d:
        d[cover].append(area)
    else:
        d[cover] = [area]
del(sc)

#Calculate the median area for each cover type.
for k, v in d.items():
    median = numpy.median(v)
    print("GCPs with order '{0}' have median Easting {1}m".format(k, median))


##>>> Polygons with cover woods have median area 83095.3479504
##Polygons with cover other have median area 55491.6260843
##Polygons with cover orch have median area 83477.7527484
