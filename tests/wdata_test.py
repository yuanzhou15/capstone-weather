
import numpy as np
import calendar
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.configDefault import config
from netCDF4 import Dataset
from datetime import datetime, timedelta
import fnmatch
import unittest
from src import wdata


class TestRadar(unittest.TestCase):
    hrs = [
        ((2017, 12, 30, 5), 'radar.20171230.05.dat'),
        ((2010, 6, 10, 0), 'radar.20100610.00.dat'),
        ((2016, 12, 26, 23), 'radar.20161226.23.dat'),
        ((2017, 12, 31, 19), None),
    ]

    def test_getHour(self):
        for arg, fname in TestRadar.hrs:
            hr1 = wdata.Radar.getHour(*arg)
            hr2 = (arg, wdata.Radar.data_read(fname))
            if fname is None:
                self.assertRaises(wdata.Radar.getHour, arg)
            else:
                self.assertTrue(TestRadar.eqHr(wdata.Radar.getHour(*arg),
                                               hr2))

    def test_getDay(self):
        pass

    def test_getMonth(self):
        pass

    def test_getYear(self):
        pass

    @staticmethod
    def eqHr(dat1, dat2):
        pass


class TestSat(unittest.TestCase):
    hfhrs = [
        ((2017, 7, 1, 3, 1, 1), 'goes13.2017.182.034519.BAND_01.nc'),
        ((2017, 7, 1, 5, 0, 6), 'goes13.2017.182.051518.BAND_06.nc'),
        ((2017, 7, 2, 5, 0, 5), None),
        ((2016, 7, 2, 5, 0, 6), None),
    ]
    days = []
    month = []

    def test_getHalfHr(self):
        for args, ncFile in TestSat.hfhrs:
            match = False
            if not ncFile:
                match = TestSat.ncDSequal(wdata.Sat.getHalfHr(*args), None)
            else:
                match = TestSat.ncDSequal(wdata.Sat.getHalfHr(*args),
                                          Dataset(config['satelliteRootPath']+ncFile, 'r'))
            self.assertTrue(match)

    def test_getDay(self):
        pass

    def test_getMonth(self):
        pass

    def test_getYear(self):
        pass

    @staticmethod
    def ncDSequal(ds1, ds2):
        if not ds1:
            return ds2 is None
        if not ds2:
            return ds1 is None

        for k in ds1.variables:
            if not k in ds2.variables:
                return False
            if type(ds1['/'+str(k)][:]) == type(np.array([])):
                if not np.array_equal(ds1['/'+str(k)][:], ds2['/'+str(k)][:]):
                    return False
            elif ds1['/'+str(k)][:] != ds2['/'+str(k)][:]:
                return False
        return True


if __name__ == '__main__':
    unittest.main()
