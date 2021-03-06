# fetchZip.py
# Purpose: Fetch a zip file and place it in an output directory.
import os, urllib2


def fetchZip(url, outputDir):
    '''Fetch binary web content located at 'url'
    and write it in the output directory'''
    response = urllib2.urlopen(url)
    binContents = response.read()
    response.close()

    # Save zip file to output dir (write it in 'wb' mode).
    outFileName = outputDir + os.path.basename(url)
    with open(outFileName, 'wb') as outf:
        outf.write(binContents)

outputDir = 'C:\Users\owner\Downloads\Sample_scripts\ch20/'
theURL = 'file:///C:\Users\owner\Downloads/GRE Big Book.zip'
fetchZip(theURL, outputDir)
print('{0}{1} created.'.format(outputDir, os.path.basename(theURL)))
