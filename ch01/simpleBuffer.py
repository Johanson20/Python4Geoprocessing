# simpleBuffer.py
import arcpy

# Buffer park.shp by 0.25 miles around each feature exterior.
# Buffers ends are rounded & all buffers are dissolved into a single feature.
arcpy.Buffer_analysis('C:/Users/owner/Downloads/Sample_scripts/ch01/Abuja_Boundary.shp',
...                       'C:/Users/owner/Downloads/Sample_scripts/ch01/parkBuffer.shp',
...                       '4.25 miles', 'OUTSIDE_ONLY', 'ROUND', 'ALL')
