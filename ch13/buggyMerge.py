# buggyMerge.py
# Purpose: Merge the dBASE tables in a directory
# Usage: No arguments needed.
import arcpy

arcpy.env.workspace = 'C:\Users\owner\Documents\Mine\Spring'
arcpy.env.overwriteOutput = True

tables = arcpy.ListTables('*', 'ALL')
output = 'Asummary.dbf'

# If the summary table already
# exists, delete it.
if arcpy.Exists(output):
	tables.remove(output)

arcpy.Merge_management(tables, output)

# This prints a success message,
# when the tool succeeds.
print arcpy.GetMessage(2)
