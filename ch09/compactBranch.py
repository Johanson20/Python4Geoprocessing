#-------------------------------------------------------------------------------
# Name:        compactBranch.py
# Purpose:     Attempts to compact local database workspace files only
#
# Author:      Johanson Onyegbula
#
# Created:     01/06/2020
#-------------------------------------------------------------------------------
import arcpy, sys, os

def main():
    file = sys.argv[1]
    desc = arcpy.Describe(file)
    if desc.dataType ==  'Workspace' and desc.workspaceType == 'LocalDatabase':
        print('File size BEFORE compact: {}'.format(os.path.getsize(file)))
        arcpy.Compact_management(file)
        print('File size AFTER compact: {}'.format(os.path.getsize(file)))
    else:
        print('Input data must be a personal or file geodatabase')
        print('Could not compact: {}'.format(os.path.basename(file)))


if __name__ == '__main__':
    main()
