# writeSimpleHTML.py
# Purpose: Write HTML page from hard-coded string.
# Usage: No arguments needed.

mystr = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Noise pollution in an environment</h1>
        <img src="../../Abstract.jpg" alt="Noise pollution">
    </body>
</html>
'''
htmlFile = 'C:\Users\owner\Downloads\Sample_scripts\ch20/output.html'
outf = open(htmlFile, 'w')
outf.write(mystr)
outf.close()
print('{0} created.'.format(htmlFile))
