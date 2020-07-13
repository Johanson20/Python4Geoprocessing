#-------------------------------------------------------------------------------
# Name:        extractMany.py
# Purpose:     UNzips every zip and kmz file from one directory to another
# Usage:       Requires two arguments - an input directory and an output directory.
#
# Author:      Johanson Onyegbula
#
# Created:     26/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, os, zipfile

def main():
    inDir = sys.argv[1]
    outDir = sys.argv[2]
    zips = os.listdir(inDir)

    for feh in zips:
        fh = os.path.join(inDir, feh)
        with zipfile.ZipFile(fh, 'r') as tempStore:
            print('Unzip {} to {}'.format(fh, outDir))
            tempStore.extractall(outDir)
            zipnames = tempStore.namelist()
            for namefh in zipnames:
                print('Extract file: {}'.format(feh))

if __name__ == '__main__':
    main()
