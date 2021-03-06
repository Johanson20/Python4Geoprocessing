# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# aggregateExport.py
# Created on: 2020-05-23 01:59:21.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Set the necessary product code
# import arcinfo


# Import arcpy module
import arcpy


# Local variables:
Input_Features = "C:\Users\owner\Downloads\Sample_scripts\ch05\NGA_adm2.shp"
Aggregation_Distance = "1500 feet"
Output_Feature_Class = "C:\Users\owner\Downloads\Sample_scripts\ch05\Aha.shp"
Output_Table = "C:\Users\owner\Downloads\Sample_scripts\ch05\Aha_Tbl"

# Process: Aggregate Polygons
arcpy.AggregatePolygons_cartography(Input_Features, Output_Feature_Class, Aggregation_Distance, "0 Unknown", "0 Unknown", "NON_ORTHOGONAL", "", Output_Table)

