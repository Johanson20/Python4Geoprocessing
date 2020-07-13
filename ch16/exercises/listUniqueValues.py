#-------------------------------------------------------------------------------
# Name:        listUniqueValues.py
# Purpose:     Uses the uniqueList function in listManager2 module to print
#              out the list of unique values in a field in a shapefile
# Usage:       Takes two arguments - a full path feature class and a text field

# Author:      Johanson Onyegbula
#
# Created:     12/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys
scriptPath = os.path.abspath(__file__)
scriptDir = os.path.dirname(scriptPath)
relPath = 'listManage'
reqPath = os.path.join(scriptDir, relPath)
sys.path.append(reqPath)

import arcpy, listManager2

def main():
    infile = sys.argv[1]
    field = sys.argv[2]


if __name__ == '__main__':
    main()
