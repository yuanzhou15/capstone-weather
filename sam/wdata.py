""" This module is the main interface between data and code that uses it """

import numpy as np
import calendar
import os
from configDefault import config


def data_read(filename):
    """ 
        when passed the full filename (path plus filename) of a deep learning dataset
        This function reads the binary data and rescales it
        reforms it from vector into array of the proper size
        rails the data off at suggested maximum and minimum values.
        Return: the radar image as numpy array or None
    """

    dims = (126, 201)   # rows, columns
    minmax = [0, 30]  # suggested data limits for display purposes

    # set minmax = [0,0] to use minimum and maximum of each file (excluding missing data)
    # [0,30] mm/hr is a good range for rainfall

    data = np.fromfile(filename, dtype='int16',
                       count=-1, sep='')  # 2 byte integers
    data = np.reshape(data, dims)

    if (np.max(data) > 0):
        # scale data to between 0 and 1 then rail off the extremes
        if (minmax[0] > 0 or minmax[1] > 0):
            data[(data < minmax[0])] = minmax[0]
            data[(data > minmax[1])] = minmax[1]
            data = (data - minmax[0])/(minmax[1] - minmax[0])
        else:
            data = (data - np.min(data))/(np.max(data) - np.min(data))
    else:
        return None
    return data


def getHour(y, m, d, h):
    """ Get a single radar image.
        Return: tuple ('yyyy-mm-dd.hh', image) """
    # todo input validation
    radarRoot = config['radarRootPath']
    if radarRoot[-1] not in ['/', '\\']:
        radarRoot += '/'
    path = '{:s}radar.{:0>4d}{:0>2d}{:0>2d}.{:0>2d}.dat'.format(
        radarRoot, y, m, d, h)
    if not os.path.isfile(path):
        return None
    return ('{:0>4d}-{:0>2d}-{:0>2d}.{:0>2d}'.format(y, m, d, h), data_read(path))


def getDay(y, m, d):
    """ returns a list of all available images in the day:
        [ ('yyyy-mm-dd.hh', image1), ('yyyy-mm-dd.hh', image2), ... ] """
    lst = []
    for i in range(24):
        image = getHour(y, m, d, i)
        if image is None:
            continue
        # yield image
        lst.append(image)
    return lst
    # return ('{:0>4d}-{:0>2d}-{:0>2d}'.format(y,m,d), lst)
    # return iter(reduce(lambda x,y: x+y, lst, []))


def getMonth(y, m):
    """ returns a list of all available images in the month:
        [ ('yyyy-mm-dd.hh', image1), ('yyyy-mm-dd.hh', image2), ... ] """
    lst = []
    for i in range(1, 1 + calendar.monthrange(y, m)[1]):
        # yield getDay(y,m,i)
        d = getDay(y, m, i)
        if not d:
            continue
        lst.extend(d)
    return lst  # reduce(lambda x,y: x+y, lst, [])


def getYear(y):
    """ returns a list of all available images in the year:
        [ ('yyyy-mm-dd.hh', image1), ('yyyy-mm-dd.hh', image2), ... ] """
    lst = []
    for i in range(1, 13):
        m = getMonth(y, i)
        if not m:
            continue
        lst.extend(m)
return lst # reduce(lambda x,y: x+y, lst, [])
