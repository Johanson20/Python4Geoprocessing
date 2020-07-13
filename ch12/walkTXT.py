# walkTXT.py
# Purpose: Walk and print the full path file names of
#    'txt' extension files in the input directory.
# Usage: input_directory
# Example: C:/gispy/data/ch12/wTest
import os, sys
mydir = sys.argv[1]
for root, dirs, files in os.walk(mydir):
    for f in files:
        if f.endswith('.shp'):
            # Print the full path file name of f
            print('{0}/{1}'.format(root, f))
