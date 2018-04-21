""" unit tests for wdata module """

import numpy as np
import calendar
import os
import sys
from netCDF4 import Dataset
from datetime import datetime, timedelta
import fnmatch
import unittest
from exceptions import IOError

# This is how we can import src module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.configDefault import config
from src import wdata


class TestRadar(unittest.TestCase):
    """ test wdata.Radar """

    hrs = [
        ((2017, 12, 30, 5), 'radar.20171230.05.dat'),
        ((2010, 6, 10, 0), 'radar.20100610.00.dat'),
        ((2016, 12, 26, 23), 'radar.20161226.23.dat'),
        ((2017, 13, 13, 13), None),
    ]

    def test_getHour(self):
        for arg, fname in self.hrs:
            if fname is None:
                self.assertIsNone(wdata.Radar.getHour(*arg))
            else:
                self.assertTrue(self.eqHr(wdata.Radar.getHour(*arg),
                                          ('{:>04d}-{:>02d}-{:0>2d}.{:0>2d}'.format(*arg), wdata.Radar.data_read(config['radarRootPath'] + fname))))

    def test_getDay(self):
        pass

    def test_getMonth(self):
        pass

    def test_getYear(self):
        pass

    @staticmethod
    def eqHr(hr1, hr2):
        """ test if two radar hours obtained using wdata.getHour() are equal based on their contents """
        if len(hr1) != len(hr2):
            return False
        if not hr1[0] == hr2[0]:
            return False
        if not (type(hr1[1]) == type(hr2[1]) == type(np.array([]))):
            return False
        return np.array_equal(hr1[1], hr2[1])


class TestSat(unittest.TestCase):
    """ test wdata.Sat """

    hfhrs = [
        ((2017, 7, 1, 3, 1, 1), 'goes13.2017.182.034519.BAND_01.nc'),
        ((2017, 7, 1, 5, 0, 6), 'goes13.2017.182.051518.BAND_06.nc'),
        ((2017, 7, 2, 5, 0, 5), None),
        ((2016, 7, 2, 5, 0, 6), None),
    ]
    days = []
    month = []

    def test_getHalfHr(self):
        for args, ncFile in self.hfhrs:
            if not ncFile:
                self.assertIsNone(wdata.Sat.getHalfHr(*args))
            else:
                self.assertTrue(self.ncDSequal(wdata.Sat.getHalfHr(*args),
                                               Dataset(config['satelliteRootPath']+ncFile, 'r')))

    def test_getDay(self):
        pass

    def test_getMonth(self):
        pass

    def test_getYear(self):
        pass

    @staticmethod
    def ncDSequal(ds1, ds2):
        """ test if two netcdf4 datasets are equal based on their contents """
        for k in ds1.variables:
            if not k in ds2.variables:
                return False
            # if k is a ndarray variable
            if type(ds1['/%s' % k][:]) == type(np.array([])):
                if not np.array_equal(ds1['/%s' % k][:], ds2['/%s' % k][:]):
                    return False
            elif ds1['/%s' % k][:] != ds2['/%s' % k][:]:
                return False
        return True


if __name__ == '__main__':
    unittest.main()
