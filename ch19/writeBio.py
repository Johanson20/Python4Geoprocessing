#-------------------------------------------------------------------------------
# Name:        writeBio.py
# Purpose:     Creates a file containing basic information about myself
#
# Author:      Johanson Onyegbula
#
# Created:     22/06/2020
#-------------------------------------------------------------------------------

def main():
    infile = open('C:\Users\owner\Downloads\Sample_scripts\ch19/mybio.txt', 'w')
    infile.write('Johanson\nArcGIS\nUmuikoro, Ngor-Okpala, Imo State\n')
    infile.write('''I am a simple, loving, intelligent young man with a Bachelors degree
     in Surveying and Geoinformatics from the University of Lagos, Nigeria''')
    infile.close()


if __name__ == '__main__':
    main()
