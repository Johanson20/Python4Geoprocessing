#-------------------------------------------------------------------------------
# Name:        writeFieldsHTML.py
# Purpose:     Creates a html file that displays the name of an input file as
#              header and a bulleted lists of all its fields
# Usage:       Requires two arguments - a full path input filename and an output
#              directory for the html file to be created.
#
# Author:      Johanson Onyegbula
#
# Created:     25/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, os, arcpy

def main():
    infile = sys.argv[1]
    outDir = sys.argv[2]
    outfile = os.path.join(outDir, 'park.html')

    with open(outfile, 'w') as fh:
        header = '<html><body><h1>{} Fields</h1><ul>'.format(os.path.basename(infile))
        fields = arcpy.ListFields(infile)
        fh.write(header)
        for field in fields:
            name = field.name
            fh.write('<li>{}</li>'.format(name))
        fh.write('</ul></body></html>')
    print('File: {} created'.format(outfile))

if __name__ == '__main__':
    main()
