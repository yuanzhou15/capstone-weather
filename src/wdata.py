""" This module is the main interface between weather data and code that uses it """

import numpy as np
import calendar
import os
from configDefault import config, cached_listdir_sat
from netCDF4 import Dataset
from datetime import datetime, timedelta
import fnmatch


class Radar:
    @staticmethod
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

    @staticmethod
    def getHour(y, m, d, h):
        """ Get a single radar image.
            Return: tuple ('yyyy-mm-dd.hh', image as ndarray) """
        # todo input validation
        radarRoot = config['radarRootPath']
        if radarRoot[-1] not in ['/', '\\']:
            radarRoot += '/'
        path = '{:s}radar.{:0>4d}{:0>2d}{:0>2d}.{:0>2d}.dat'.format(
            radarRoot, y, m, d, h)
        if not os.path.isfile(path):
            return None
        return ('{:0>4d}-{:0>2d}-{:0>2d}.{:0>2d}'.format(y, m, d, h), Radar.data_read(path))

    @staticmethod
    def getDay(y, m, d):
        """ returns a list of all available images in the day:
            [ ('yyyy-mm-dd.hh', image1), ('yyyy-mm-dd.hh', image2), ... ] """
        lst = []
        for i in range(24):
            image = Radar.getHour(y, m, d, i)
            if image is None:
                continue
            # yield image
            lst.append(image)
        return lst
        # return ('{:0>4d}-{:0>2d}-{:0>2d}'.format(y,m,d), lst)
        # return iter(reduce(lambda x,y: x+y, lst, []))

    @staticmethod
    def getMonth(y, m):
        """ returns a list of all available images in the month:
            [ ('yyyy-mm-dd.hh', image1), ('yyyy-mm-dd.hh', image2), ... ] """
        lst = []
        for i in range(1, 1 + calendar.monthrange(y, m)[1]):
            # yield getDay(y,m,i)
            d = Radar.getDay(y, m, i)
            if not d:
                continue
            lst.extend(d)
        return lst  # reduce(lambda x,y: x+y, lst, [])

    @staticmethod
    def getYear(y):
        """ returns a list of all available images in the year:
            [ ('yyyy-mm-dd.hh', image1), ('yyyy-mm-dd.hh', image2), ... ] """
        lst = []
        for i in range(1, 13):
            m = Radar.getMonth(y, i)
            if not m:
                continue
            lst.extend(m)
        return lst  # reduce(lambda x,y: x+y, lst, [])


class Sat:
    @staticmethod
    def getHalfHr(y, m, d, hr, halfhr, band):
        """ Get satellite data for a specific half-hour and band
            which corressponde to a unique .nc file in the satallite dataset.

            halfhr: 0 or 1 for first or second half hour
            Sspecific minute is assumed to be 15 or 45.
            Specific second is automatically guessed from filenames

            Return: netcdf4 dataset or None """

        # todo: input validation
        satRoot = config['satelliteRootPath']
        if satRoot[-1] not in ['/', '\\']:
            satRoot += '/'

        # convert given date to day sequence number in year
        daynum = reduce(lambda x, y: x+y,
                        map(lambda x: calendar.monthrange(2017, x)[1], range(1, m)), d)

        # find the seconds used in the filename
        # it is assumed the minutes part is always "15" or ""
        targetFilename = u'goes13\.{:0>4d}\.{:0>3d}\.{:0>2d}{:s}??\.BAND_{:0>2d}\.nc'.format(
            y, daynum, hr, ['15', '45'][halfhr], band).replace(u'??', u'[0-9]{2}')
        # print targetFilename
        path = None
        import re
        for file in cached_listdir_sat:
            # todo: this should be cached

            match = re.findall(
                targetFilename.replace(u'??', u'[0-9]{2}'), file)
            # if fnmatch.fnmatch(file, targetFilename):
            if match:
                path = satRoot + file
                break

        if not path:
            return None
        return Dataset(path, mode='r')

    @staticmethod
    def getDay(y, m, d, band):
        lst = []
        for i in range(24):
            hh1 = Sat.getHalfHr(y, m, d, i, 0, band)
            hh2 = Sat.getHalfHr(y, m, d, i, 1, band)
            if hh1:
                lst.append(hh1)
            if hh2:
                lst.append(hh2)
        return lst

    @staticmethod
    def getMonth(y, m, band):
        lst = []
        for i in range(1, 1 + calendar.monthrange(y, m)[1]):
            lst.extend(Sat.getDay(y, m, i, band))
        return lst

    @staticmethod
    def getYear(y, band):
        lst = []
        for i in range(1, 13):
            lst.extend(Sat.getMonth(y, i, band))
        return lst

    @staticmethod
    def getAndClose(ds, var='data'):
        """
            Since netcdf files keep file handles open, loading too many files at once without closing them isn't possible.
            Use this method to read a target variable from netcdf dataset and close it promptly.
            Example:
            band2 = [getAndClose(ds) for ds in getMonth(2017, 7, 2)]
        """
        dat = ds['/%s' % var][0]
        ds.close()
        return dat
