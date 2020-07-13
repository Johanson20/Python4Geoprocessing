# simplifyOops1.py
# Purpose: Create simplified polygons for all of the valid polygon files
#          and print a warning if it fails for one of the files.
# Usage: No arguments needed.
# Warning: This script contains an error!

import arcpy, os
arcpy.env.workspace = 'C:/Users/owner/Downloads/Sample_scripts/ch07/'
arcpy.env.overwriteOutput = True
outDir = 'C:/Users/owner/Downloads/Sample_scripts/ch07/chichui/'
if not os.path.exists(outDir):
    os.mkdir(outDir)

fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    try:
        count = arcpy.SimplifyPolygon_cartography(fc, outDir + fc, '#', 100)
        print('{0} has been simplified.'.format(fc))
    except arcpy.ExecuteError:
        print(arcpy.GetMessages())
