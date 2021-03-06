# areaMedian.py
# Purpose: Find the polygon median area and identify polygons
#          with areas in this range.
# Usage: No arguments needed.
import arcpy, numpy

fc = 'C:\Users\owner\Downloads\Sample_scripts\ch07\shapefiles/boundingBoxes.shp'
idField = 'FID'
areaField = 'Geom1'
areasDict = {}

# User search cursor to populate id:area dictionary items.
sc = arcpy.da.SearchCursor(fc, [idField, areaField])
for row in sc:
    id = row[0]
    area = row[1]
    areasDict[id] = area
del(sc)

# Find the median area.
areas = areasDict.values()
medianArea = numpy.median(areas)
print('Median area: {0}'.format(medianArea))

# Find the polygons with values close to median.
sqArea = 100
print('Polygons close to median:')
for k, v in areasDict.items():
    if (medianArea - sqArea) < v < (medianArea + sqArea):
        print('{0}: {1}, {2}: {3}'.format(idField, k, areaField, v))
