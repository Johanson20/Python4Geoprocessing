#-------------------------------------------------------------------------------
# Name:        writeRastersHTML.py
# Purpose:     Creates a html file with a relative link to every image in
#              a directory containing images and displays the images
# Usage:       Requires two arguments - a directory containing images and an output
#              directory for the html file to be created.
#
# Author:      Johanson Onyegbula
#
# Created:     25/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, os

def main():
    rasterDir = sys.argv[1]
    outDir = sys.argv[2]
    infile = os.path.join(outDir, 'rasters.html')

    with open(infile, 'w') as fh:
        header = '<html><body><h1>Rasters in {}</h1><ul>'.format(rasterDir)
        fh.write(header)
        rasters = os.listdir(rasterDir)
        for rast in rasters:
            fh.write('<li>{}</li>'.format(os.path.splitext(rast)[0]))
        fh.write('</ul></body></html>')
    print('File: {} created'.format(infile))

if __name__ == '__main__':
    main()
