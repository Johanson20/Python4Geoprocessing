#-------------------------------------------------------------------------------
# Name:        nameWalk.py
# Purpose:     Walks through a folder and prints files whose names contain
#              at least two occurrences of 'a'
#
# Author:      Johanson Onyegbula
#
# Created:     06/06/2020
#-------------------------------------------------------------------------------
import os, sys

def main():
    indir = sys.argv[1]
    for directory, subdir, files in os.walk(indir):
        for f in files:
            if f.find('a') > -1 and f.rfind('a') != f.find('a'):
                print(f)

if __name__ == '__main__':
    main()
