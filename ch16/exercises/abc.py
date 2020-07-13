#-------------------------------------------------------------------------------
# Name:        abc
# Purpose:     Imports reportArgs module and calls printArgs function
#
# Author:      Johanson Onyegbula
#
# Created:     12/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys

scriptPath = os.path.abspath(__file__)
scriptDir = os.path.dirname(scriptPath)
relPath = '../../ch15'
reportArgsPath = os.path.join(scriptDir, relPath)
sys.path.append(reportArgsPath)

import reportArgs
reportArgs.printArgs()


def main():
    pass

if __name__ == '__main__':
    main()
