# simplifyOops2.py
# Purpose:  Simplify polygons using ten different minimum area values.
# Output:   Should create 10 output shapefiles.
# Warning: This code contains errors!
import arcpy, os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/Users/owner/Downloads/Sample_scripts/ch07/'

outDir = 'C:/Users/owner/Downloads/Sample_scripts/ch07/chichi/'
if not os.path.exists(outDir):
    os.mkdir(outDir)

fc = 'boundingBoxes.shp'
x = 1
while x <= 10:
    try:
        output = '{0}{1}{2}Simp.shp'.format(outDir, fc[:-12], x)
        minArea = '{0}'.format(x)
        arcpy.SimplifyPolygon_cartography(fc, output, '#', minArea)
        print('Created: {0}'.format(output))
    except arcpy.ExecuteError:
        print(arcpy.GetMessages())
    x = x + 1
