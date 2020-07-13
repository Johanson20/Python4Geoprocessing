import os, sys

scriptPath = os.path.abspath(__file__)
scriptDir = os.path.dirname(scriptPath)
relativePath = '../'
modulePathA = os.path.join(scriptDir, relativePath)
sys.path.append(modulePathA)

#scriptB resides in the same directory as this file, so no need to append path
#appends path for scriptC for import
molulePathC = os.path.join(scriptDir, 'simpleScripts')
sys.path.append(molulePathC)

#appends path for scriptD for import
molulePathD = os.path.join(molulePathC, 'moreSimpleScripts')
sys.path.append(molulePathD)

#appends path for scriptE for import
molulePathE = os.path.join(scriptDir, relativePath + 'exerSupportCode')
sys.path.append(molulePathE)

import scriptA, scriptB, scriptC, scriptD, scriptE
