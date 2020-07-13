# near.py
# Purpose: Compute the set of features that are near
#          to another set of features based on a search radius.
#          Also, illustrate passing arguments that
#          include file paths.

import arcpy, sys

# Get user arguments.
input_features = sys.argv[1]
if input_features == '#':
    # Set a default value if unspecified.
    input_features = 'C:\Users\owner\Downloads\Sample_scripts\ch06\Lagos_GPS_GCPs.shp'

near_features = sys.argv[2]
if near_features == '#':
    # Set a default value if unspecified.
    near_features = 'C:\Users\owner\Downloads\Sample_scripts\ch06\Lagos_GPS_GCPs.shp'

search_radius = sys.argv[3]
if search_radius == '#':
    # Set a default value if unspecified.
    search_radius = '2 Miles'

# Call near analysis tool.
arcpy.Near_analysis(input_features, near_features,
                    search_radius, 'NO_LOCATION', 'NO_ANGLE')
print(arcpy.GetMessages())
