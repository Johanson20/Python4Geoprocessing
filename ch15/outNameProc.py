# outNameProc.py
# Purpose: Print output file names derived from input file names.
# Usage: No script arguments required.
import os

def outName(infile, prestring = 'Out', extension = 'shp', outDir = ''):
    """Dynamically creates output file names based on input filenames.
        infile is the name of the input file, possibly with its full path.
        prestring is the name of the optional string attached before the
        output file extension; default value is 'Out.
        extension is the extension of the output file to be created;
        default extension is 'shp'.
        outDir is the name of the output directory where the output file
        would be stored in, default is a null string, which stores
        outputs in the input directory."""
    basename = os.path.basename(infile)
    outfile = os.path.splitext(basename)[0] + prestring + '.' + extension
    if outDir:
        outputFilename = os.path.join(outDir, outfile)
    else:
        outputFilename = outfile
    return outputFilename


input1 = 'C:/Data/NC.shp'
input2 = 'Raleigh.shp'
input3 = 'parks'

outDir1 = 'C:/gispy/scratch'
outDir2 = 'C:/spam/'
outDir3 = 'C:/foo/'

# Set feature to point output name.
centroids = outName(input1, 'Points', 'shp', outDir1)
print(centroids)

# Set central feature output name.
centralFeature = outName(input1, 'Central', 'shp', outDir2)
print(centralFeature)

# Set mean center output name.
meanCenter = outName(input1, 'Mean')
print(meanCenter)

# Set point distance output name.
distanceTable = outName(input1, 'Mean2Central', 'dbf')
print(distanceTable)

# Set generic output name.
myoutput = outName(input2)
print(myoutput)

# Set polygon distribution output name.
distributionFile = outName(input3, 'Distribution', 'txt', outDir3)
print(distributionFile)

#### Output in Interactive Window should look like this:

###C:/gispy/scratch\NCPoints.shp
###C:/spam/NCCentral.shp
###NCMean.shp
###NCMean2Central.dbf
###RaleighOut.shp
###C:/foo/parksDistribution.txt