#-------------------------------------------------------------------------------
# Name:        handlePaths
# Purpose:     Manipulates files based on two input arguments, a path and
#              base file in the same directory
#
# Author:      Johanson Onyegbula
#
# Created:     24/05/2020
#-------------------------------------------------------------------------------
import os, sys

def main():
    fullPath = sys.argv[1]
    baseName = sys.argv[2]
    os.path.basename(fullPath)
    (c1, c2) = os.path.splitext(baseName)
    (c3, c4) = os.path.split(fullPath)
    baseFile = os.path.join(c3, baseName)
    fileSize = os.path.getsize(baseFile)
    directory = os.listdir(c3)

    #prints outputs
    print('The first file is: {0}\nThe first file extension is {1}\nThe full name of the second file is {2}'.format(baseName, c2, baseFile))
    print('The size of the second file is: {} bytes'.format(fileSize))
    print('{} contains the following files: \n{}'.format(c3, directory))


if __name__ == '__main__':
    main()
