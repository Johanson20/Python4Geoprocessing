#-------------------------------------------------------------------------------
# Name:        batchAscii2Raster.py
# Purpose:     Converts one or more ASCII input files to Raster files
#
# Author:      Johanson Onyegbula
#
# Created:     01/07/2020
#-------------------------------------------------------------------------------
import os, tkFileDialog, Tkinter, arcpy

tkBox = Tkinter.Tk()
tkBox.withdraw()

infile = tkFileDialog.askopenfilename(initialdir='C:\Users\owner\Downloads\Sample_scripts\ch22',
parent=tkBox, title='Select at least one ESRI ASCII file', initialfile='park.shp', multiple=True,
filetypes=[('ASCII Files', '*.asc'), ('ASCII Textfiles', '*.txt')])

print('User selections: {}'.format(infile.split(' ')))

arcpy.env.workspace = os.path.dirname(infile)
t = 0
for filename in infile.split(' '):
    outname = 'out{}'.format(t)
    t = t + 1
    arcpy.ASCIIToRaster_conversion(infile, outname)
    print('Created output raster: {}'.format(os.path.abspath(outname)))
tkBox.destroy()
