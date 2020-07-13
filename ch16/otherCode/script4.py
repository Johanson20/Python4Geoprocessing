import sys, os
scriptPath = os.path.abspath(__file__)
scriptDir = os.path.dirname(scriptPath)
relativePath = '../../ch15'
modulePath= os.path.join(scriptDir, relativePath)
sys.path.append(modulePath)
import punctuationArt

print('Inside script4')
print(os.path.abspath(__file__))