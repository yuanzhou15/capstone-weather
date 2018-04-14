
import numpy as np
import calendar
import os
from src.configDefault import config
from netCDF4 import Dataset
from datetime import datetime, timedelta
import fnmatch
import unittest
import src.wdata as wdata


class TestRadar(unittest.TestCase):
    pass


class TestSat(unittest.TestCase):
    hfhrs = [
        ((2017, 7, 2, 3, 1, 1), 'goes13.2017.182.034519.BAND_01.nc'),
        ((2017, 7, 2, 5, 0, 6), 'goes13.2017.182.051518.BAND_06.nc'),
        ((2017, 7, 2, 5, 0, 5), None),
        ((2016, 7, 2, 5, 0, 6), None),
    ]
    days = []
    month = []

    def test_getHalfHr(self):
        for args, ncFile in TestSat.hfhrs:
            TestSat.ncDSequal(Dataset(wdata.Sat.getHalfHr(*args), 'r'),
                              Dataset(config['satelliteRootPath']+ncFile, 'r'))

    def test_getDay(self):
        pass

    def test_getMonth(self):
        pass

    def test_getYear(self):
        pass

    @staticmethod
    def ncDSequal(ds1, ds2):
        pass
