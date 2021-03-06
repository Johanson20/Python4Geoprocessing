#-------------------------------------------------------------------------------
# Name:        writeHTML3.py
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
    imageDir = sys.argv[1]
    outDir = sys.argv[2]
    infile = os.path.join(outDir, 'images3.html')

    with open(infile, 'w') as fh:
        fh.write('<html><body><h1>Pics</h1>')
        images = os.listdir(imageDir)
        imgPath = os.path.relpath(imageDir, outDir)
        for img in images:
            fh.write('<img href src="{0}\{1}" alt={2} width="287" height="165">'.format(imgPath, img, os.path.splitext(img)[0]))
        fh.write('</body></html>')
    print('File: {} created'.format(infile))

if __name__ == '__main__':
    main()
