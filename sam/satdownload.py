#!/usr/bin/env python

""" 
    Download Satellite data given save path and bands.
    Already existing files won't be re-downloaded.
    Must be run from command line!
    Example to download bands 2 and 3 to ~/sat/ run
    $ python2 satdownload.py ~/sat/ 2 3

    p.s. You need to have requests installed:
    $ pip2 install requests 
"""

from urllib2 import urlopen
import re
import os
import argparse
import requests
import sys

html = urlopen('http://water.ccny.cuny.edu/pubs/irina/goes13/')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('destination', type=str,
                        help='destination directory where files will be downloaded')
    parser.add_argument('bands', metavar='B', type=int, nargs='+',
                        help='an integer for the accumulator')
    arg = parser.parse_args()
    try:
        bands, dest = arg.bands, os.path.abspath(arg.destination)
        if dest[-1] not in ['/', '\\']:
            dest += '/'
        if not os.path.isdir(dest):
            raise Exception()
    except:
        print('INAVLID DESTINATION')
        sys.exit(0)

    print 'downloading bands {:s} to {:s} \n(will only download missing files)'.format(
        str(bands), dest)
    bands = ''.join(map(str, bands))
    exist = set(os.listdir(dest))
    ncfiles = set()
    for x in html:
        pattern = u'goes13\.[0-9]{4}\.[0-9]{3}\.[0-9]{6}\.BAND_0['+bands+']\.nc'
        match = re.findall(pattern, x)
        if match:
            ncfiles = ncfiles | set(match)
    missing = ncfiles - exist
    print 'downloading %d missing files:' % len(missing)
    # start downloading:
    for i, nc in enumerate(missing):
        with open(dest+nc, 'wb') as f:
            req = requests.get(
                'http://water.ccny.cuny.edu/pubs/irina/goes13/'+nc)
            f.write(req.content)
        print '%d/%d' % (i+1, len(missing))
    print 'DONE!'
