# cfactorModify.py
# Purpose: Demonstrate reading and writing files.
# IUsage: No arguments required.  Input file hard-coded.
# Output: Modified text file *v2.txt

import os, shutil

infile = 'C:\Users\owner\Downloads\Sample_scripts\ch19/cfactors.txt'
baseN = os.path.basename(infile)
outfile = 'C:\Users\owner\Downloads\Sample_scripts\ch19/' + os.path.splitext(baseN)[0] + 'v2.txt'
try:
    # OPEN the input and output files.
    with open(infile, 'r') as fin:
        with open(outfile, 'w') as fout:
            # READ/MODIFY/WRITE the first line.
            line = fin.readline()
            line = line.replace(' ', ',')
            fout.write(line)

            # FOR the remaining lines.
            for line in fin:
                # MODIFY the line.
                line = line.replace('=', ',')
                # WRITE to output.
                fout.write(line)
            print('{0} created.'.format(outfile))
    shutil.move(outfile, infile)
except IOError:
    print("{0} doesn't exist.".format(infile))
