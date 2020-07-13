#-------------------------------------------------------------------------------
# Name:        bufferDialog.py
# Purpose:     Creates buffer about a shapefile, using inputs from GUI
#
# Author:      Johanson Onyegbula
#
# Created:     01/07/2020
#-------------------------------------------------------------------------------
import arcpy, tkFileDialog, Tkinter

tkBox = Tkinter.Tk()
tkBox.withdraw()

infile = tkFileDialog.askopenfilename(initialfile='park.shp', filetypes=[('shapefiles', '*.shp')],
initialdir='C:\Users\owner\Downloads\Sample_scripts\ch22',
parent=tkBox, title='Enter input shapefile for buffering')

outfile = tkFileDialog.asksaveasfilename(initialfile='out.shp',
initialdir='C:\Users\owner\Downloads\Sample_scripts\ch22', parent=tkBox,
filetypes=[('shapefiles', '*.shp')], title='Enter output buffer shapefile name')

bufferDist = raw_input('Enter buffer distance with units:')

tkBox.destroy()
arcpy.Buffer_analysis(infile, outfile, bufferDist)
print('{} buffer shapefile: {} created.'.format(bufferDist, outfile))
