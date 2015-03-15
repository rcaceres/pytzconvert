import unittest
import pytz

from dateutil import parser

import pytzconvert

class PytzConvertTestCase(unittest.TestCase):
 
    def setUp(self):
        pass
        
    def test_from_time_string_daylight_savings(self):
        """
        Daylight Saving Time (United States) 2015 began at 2:00 AM on
        Sunday, March 8
        and ends at 2:00 AM on
        Sunday, November 1
        """
        dt_str = "2013-09-05T01:00:00-07:00" 
        dt = parser.parse(dt_str)
        dt_converted = pytzconvert.convert(dt)
        self.assertEqual(dt_converted.tzinfo.__str__(), pytz.timezone('US/Pacific').__str__())
        self.assertEqual(dt, dt_converted)
        self.assertEqual(dt_converted.year, 2013)
        self.assertEqual(dt_converted.month, 9)
        self.assertEqual(dt_converted.day, 5)
        self.assertEqual(dt_converted.hour, 1)
        self.assertEqual(dt_converted.minute, 0)
        self.assertEqual(dt_converted.second, 0)
        
        dt_str = "2013-08-11T01:00:00-07:00"
        dt = parser.parse(dt_str)
        dt_converted = pytzconvert.convert(dt)
        self.assertEqual(dt_converted.tzinfo.__str__(), pytz.timezone('US/Pacific').__str__())
        self.assertEqual(dt, dt_converted)
        self.assertEqual(dt_converted.year, 2013)
        self.assertEqual(dt_converted.month, 8)
        self.assertEqual(dt_converted.day, 11)
        self.assertEqual(dt_converted.hour, 1)
        self.assertEqual(dt_converted.minute, 0)
        self.assertEqual(dt_converted.second, 0)
        
        dt_str = "2013-09-15T20:00:00-07:00"
        dt = parser.parse(dt_str)
        dt_converted = pytzconvert.convert(dt)
        self.assertEqual(dt_converted.tzinfo.__str__(), pytz.timezone('US/Pacific').__str__())
        self.assertEqual(dt, dt_converted)
        self.assertEqual(dt_converted.year, 2013)
        self.assertEqual(dt_converted.month, 9)
        self.assertEqual(dt_converted.day, 15)
        self.assertEqual(dt_converted.hour, 20)
        self.assertEqual(dt_converted.minute, 0)
        self.assertEqual(dt_converted.second, 0)


    def test_from_time_string_not_daylight_savings(self):
        dt_str = "2013-12-05T17:00:00-08:00"
        dt = parser.parse(dt_str)
        dt_converted = pytzconvert.convert(dt)
        self.assertEqual(dt_converted.tzinfo.__str__(), pytz.timezone('US/Pacific').__str__())
        self.assertEqual(dt, dt_converted)
        self.assertEqual(dt_converted.year, 2013)
        self.assertEqual(dt_converted.month, 12)
        self.assertEqual(dt_converted.day, 5)
        self.assertEqual(dt_converted.hour, 17)
        self.assertEqual(dt_converted.minute, 0)
        self.assertEqual(dt_converted.second, 0)
        
        dt_str = "2013-12-05T12:00:00-08:00"
        dt = parser.parse(dt_str)
        dt_converted = pytzconvert.convert(dt)
        self.assertEqual(dt_converted.tzinfo.__str__(), pytz.timezone('US/Pacific').__str__())
        self.assertEqual(dt, dt_converted)
        self.assertEqual(dt_converted.year, 2013)
        self.assertEqual(dt_converted.month, 12)
        self.assertEqual(dt_converted.day, 5)
        self.assertEqual(dt_converted.hour, 12)
        self.assertEqual(dt_converted.minute, 0)
        self.assertEqual(dt_converted.second, 0)

        
        dt_str = "2014-01-04T20:00:00-08:00"
        dt = parser.parse(dt_str)
        dt_converted = pytzconvert.convert(dt)
        self.assertEqual(dt_converted.tzinfo.__str__(), pytz.timezone('US/Pacific').__str__())
        self.assertEqual(dt, dt_converted)
        self.assertEqual(dt_converted.year, 2014)
        self.assertEqual(dt_converted.month, 1)
        self.assertEqual(dt_converted.day, 4)
        self.assertEqual(dt_converted.hour, 20)
        self.assertEqual(dt_converted.minute, 0)
        self.assertEqual(dt_converted.second, 0)
        


    def test_us_eastern_not_daylight_savings(self):
        dt_str = "2012-11-28T20:00:00-05:00"
        dt = parser.parse(dt_str)
        dt_converted = pytzconvert.convert(dt)
        self.assertEqual(dt_converted.tzinfo.__str__(), pytz.timezone('US/Eastern').__str__())
        self.assertEqual(dt, dt_converted)
        self.assertEqual(dt_converted.year, 2012)
        self.assertEqual(dt_converted.month, 11)
        self.assertEqual(dt_converted.day, 28)
        self.assertEqual(dt_converted.hour, 20)
        self.assertEqual(dt_converted.minute, 0)
        self.assertEqual(dt_converted.second, 0)
        
    def test_us_eastern_daylight_savings(self):
        dt_str = "2013-05-21T08:30:00-04:00"
        dt = parser.parse(dt_str)
        dt_converted = pytzconvert.convert(dt)
        self.assertEqual(dt_converted.tzinfo.__str__(), pytz.timezone('US/Eastern').__str__())
        self.assertEqual(dt, dt_converted)
        self.assertEqual(dt_converted.year, 2013)
        self.assertEqual(dt_converted.month, 5)
        self.assertEqual(dt_converted.day, 21)
        self.assertEqual(dt_converted.hour, 8)
        self.assertEqual(dt_converted.minute, 30)
        self.assertEqual(dt_converted.second, 0)
