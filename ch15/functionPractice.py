# functionPractice.py
# Purpose: Print information separated by fish punctuation art
#          for each polygon feature class in the input workspace.
# Usage: input_workspace
# Example input: C:/gispy/data/ch15/tester.gdb
import arcpy, sys

def printFish():
    print('''  ,,,
             <')}>)={
               ``''')

def printDescription(filename):
    '''Describes some properties of a file'''
    desc = arcpy.Describe(filename)
    print('Name:\t\t\t{}\nType:\t\t\t{}\nCatalog path:\t{}\n'.format(desc.name, desc.dataType, desc.path))

workspace = sys.argv[1]
arcpy.env.workspace = workspace
features = arcpy.ListFeatureClasses()
for feature in features:
    printFish()
    printDescription(feature)

##Pseudocode:
##IMPORT arcpy
##
##PROC printFish
##    PRINT a fish
##
##PROC printDescription(filename)
##    GET a describe object
##    PRINT name
##    PRINT type
##    PRINT catalog path
##
##SET the workspace to the user argument
##GET a list of polygon feature classes
##FOR each file in list
##    CALL printfish
##    CALL printDescription with the current file as the argument




#-----------------------------------------
## For example input: C:/gispy/data/ch15/tester.gdb
## Output should look like this:
##  ,,,
##<')}>)={
##  ``
##
##Name:        park
##DataType:        FeatureClass
##CatalogPath:        C:/gispy/data/ch15/tester.gdb/park
##
##  ,,,
##<')}>)={
##  ``
##
##Name:        regions2
##DataType:        FeatureClass
##CatalogPath:        C:/gispy/data/ch15/tester.gdb/regions2
##
##  ,,,
##<')}>)={
##  ``
##
##Name:        workzones
##DataType:        FeatureClass
##CatalogPath:        C:/gispy/data/ch15/tester.gdb/workzones
##
##  ,,,
##<')}>)={
##  ``
##
##Name:        regions1
##DataType:        FeatureClass
##CatalogPath:        C:/gispy/data/ch15/tester.gdb/regions1
##
##  ,,,
##<')}>)={
##  ``
##
##Name:        smallWoods2
##DataType:        FeatureClass
##CatalogPath:        C:/gispy/data/ch15/tester.gdb/smallWoods2
