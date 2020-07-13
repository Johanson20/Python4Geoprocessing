#-------------------------------------------------------------------------------
# Name:        parseHTMLimages.py
# Purpose:     Displays the number of images in given url
# Usage:       Requires one argument: a url.
#
# Author:      Johanson Onyegbula
#
# Created:     25/06/2020
# Copyright:   (c) owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, os, BeautifulSoup, urllib2

def main():
    url = sys.argv[1]
    response = urllib2.urlopen(url)
    soup = BeautifulSoup.BeautifulSoup(response.read())
    imgs = soup.findAll('img')
    noImg = len(imgs)
    print('{} images found.'.format(noImg))
    for img in imgs:
        print('image src:{};'.format(img['src']))

if __name__ == '__main__':
    main()
