# csvStrings.py

import os, sys
scriptPath = os.path.abspath(__file__)
scriptDir = os.path.dirname(scriptPath)
relPath = 'listManage'
reqPath = os.path.join(scriptDir, relPath)
sys.path.append(reqPath)

import listManager3

wheatYield = [
    '1,4.07,4.21,4.15,4.64,4.03,3.74,4.56',
    '2,,4.29,4.4,4.69,3.77,4.46,4.76',
    '3,3.9,4.64,4.05,4.04,3.49,3.91,4.52',
    '4,3.63,,4.92,4.64,3.75,4.1,4.4',
    '5,3.15,,4.08,4.73,3.61,3.66,'
]

for i, value in enumerate(wheatYield):
    print('Site {} has {} samples: {}'.format(i+1, listManager3.delimStrLen2(',', value), value))
