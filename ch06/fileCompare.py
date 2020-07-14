#-------------------------------------------------------------------------------
# Name:        fileCompare
# Purpose:     Compares the contents of two ASCII text files for similarity
#
# Author:      Johanson Onyegbula
#
# Created:     24/05/2020
#-------------------------------------------------------------------------------
import arcpy, sys, os

def main():
    inFeature1 = sys.argv[1]
    inFeature2 = sys.argv[2]
    outFeature = sys.argv[3]

    result = arcpy.FileCompare_management(inFeature1, inFeature2, outFeature)
    print('Comparison results have been written to: \n{}'.format(outFeature))
    print('Are the input files ({} and {}) the same? {}'.format(os.path.basename(inFeature1), os.path.basename(inFeature2), result.getOutput(1)))


if __name__ == '__main__':
    main()
