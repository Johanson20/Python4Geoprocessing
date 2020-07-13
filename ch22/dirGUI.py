#-------------------------------------------------------------------------------
# Name:        dirGUI.py
# Purpose:     Prints all rasters in a directory selected from a simple GUI
#
# Author:      Johanson Onyegbula
#
# Created:     01/07/2020
#-------------------------------------------------------------------------------
import os, tkFileDialog, Tkinter

tkBox = Tkinter.Tk()
tkBox.withdraw()

inDir = tkFileDialog.askdirectory(initialdir='C:\Users\owner\Downloads\Sample_scripts\ch22',
parent=tkBox, title='Select a raster directory')
print('Directory = {}'.format(inDir))

files = os.listdir(inDir)
tkBox.destroy()

listofFiles = []
for filename in files:
    listofFiles.append(filename)
print(listofFiles)
