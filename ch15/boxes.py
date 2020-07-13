# boxes.py
# Usage: No arguments required
import arcpy, os

def findPerimeter(length, width):
    '''Find the perimeter of a box'''
    return 2*length + 2*width

def isSquare(length, width):
    '''Check if the box is square'''
    if length == width:
        ans = True
    else:
        ans = False
    return ans

def createBoundingBoxes(inspace, outdir):
    '''Create a minimum bounding box feature class
        for each polgon feature class in the workspace'''
    arcpy.env.workspace = inspace
    features = arcpy.ListFeatureClasses('*', 'Polygon')
    for feature in features:
        outName = + os.path.splitext(feature)[0] + 'Bound.shp'
        try:
            arcpy.MinimumBoundingGeometry_management(feature, outName)
            print('{} created'.format(outName))
        except:
            arcpy.GetMessages()

#############################
length = 3
width = 6

print(findPerimeter(length, width))
print(isSquare(length, width))

#############################
# Set box
length = 5
width = 5

print(findPerimeter(length, width))
print(isSquare(length, width))

#############################
# Create a minimum bounding box feature class
# for each polgon feature class in the workspace
workspace = 'C:/gispy/data/ch15'
outDir = 'C:/gispy/data/ch15/scratch'
createBoundingBoxes(workspace, outDir)

#############################
# Create a minimum bounding box feature class
# for each polgon feature class in the workspace
workspace = 'C:/gispy/data/ch15/tester.gdb'
outDir = 'C:/gispy/scratch/'
createBoundingBoxes(workspace, outDir)
