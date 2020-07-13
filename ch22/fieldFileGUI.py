#-------------------------------------------------------------------------------
# Name:        fieldFileGUI.py
# Purpose:     Prints all fields in an input shapefile or dBase file selected from a GUI
#
# Author:      Johanson Onyegbula
#
# Created:     01/07/2020
#-------------------------------------------------------------------------------
import arcpy, tkFileDialog, Tkinter

tkBox = Tkinter.Tk()
tkBox.withdraw()

infile = tkFileDialog.askopenfilename(initialdir='C:\Users\owner\Downloads\Sample_scripts\ch22',
parent=tkBox, title='Pick a file', filetypes=[('dBase Files', '*.dbf'), ('shapefiles', '*.shp')],
initialfile='park.shp')

print('{} has the following fields:'.format(infile))

with arcpy.da.SearchCursor(infile, '*') as cursor:
    for field in cursor.fields:
        print('\t{}'.format(field))
tkBox.destroy()
