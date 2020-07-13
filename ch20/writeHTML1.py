import os

outDir = 'C:\Users\owner\Downloads\Sample_scripts\ch20'
header = '<html><body><h1>Two Pictures</h1>'
img1 = '<img src="../../Graphical abstract.jpg" alt="Graphical illustration of an abstract" width="600" height="350">'
img2 = '<img src="../../../Pictures/ss.png" alt="Time series graphs" width="600" height="350"></body></html>'

infile = os.path.join(outDir, 'images1.html')
with open(infile, 'w') as fh:
    fh.write(header)
    fh.write(img1)
    fh.write(img2)
print('{} created'.format(os.path.basename(infile)))
