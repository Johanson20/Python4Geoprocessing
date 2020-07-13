# buggyFreq.py
# Purpose: Find frequency of each value in each string field

import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:\Users\owner\Downloads\Sample_scripts\ch06\shapefiles'
featureList = arcpy.ListFeatureClasses()

for inputFile in featureList:
    fields = arcpy.ListFields(inputFile, '*', 'String')
    for field in fields:
        fieldName = field.name
        outTable = inputFile + fieldName + 'freq'
        arcpy.Frequency_analysis(inputFile, outTable, fieldName)
        print('Output table created: {0}'.format(outTable))
