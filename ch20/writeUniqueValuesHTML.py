# writeUniqueValuesHTML.py
# Purpose: Write an HTML file with a list of distinct values in a field.
# Usage: No arguments required.

import arcpy, os, listManager4

baseDir = 'C:\Users\owner\Downloads/'
fc = 'Sample_scripts\ch06\shapefiles/Lagos_GPS_GCPs.shp'
fcBase = os.path.basename(fc)
fieldname = 'Control_Or'
image = '../../Graphical abstract.jpg'

### Get all values for the given field, using a search cursor
cursor = arcpy.da.SearchCursor(baseDir + fc, fieldname)
ll = []
for row in cursor:
    ll.append(row[0])

### Get unique values for the given field, using a listManager4.py function
uniqueList = listManager4.uniqueList(ll)
### Get an HTML bulleted list of the unique values, using a listManager4.py function
htmlBul = listManager4.python2htmlList(uniqueList, 'ul')
### Create HTML body with HTML bulleted list and embedded image
body = '{}<img src="{}" alt="Graphical abstract illustration">'.format(htmlBul, image)
# Create header with dynamic title.
beginning = """<!DOCTYPE html>
<html>
 <body>
  <h1> Unique values in {0} field {1}: </h1>
""".format(fcBase, fieldname)

# Create footer to close body and html tags.
end = """
 </body>
</html>
"""
outfile = baseDir + 'Sample_scripts\ch20/DataReport.html'
outf = open(outfile, 'w')
outf.write(beginning)
### Write the body to the output file
outf.write(body)
outf.write(end)
outf.close()
print('{0} created.'.format(outfile))
