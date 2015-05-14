#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
import pprint
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    data = {}
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    COAST = sheet.col_values(1, start_rowx=1)
  
    maxvalue = max(COAST)
    maxtime = sheet.cell_value(COAST.index(maxvalue) + 1, 0)
    minvalue = min(COAST)
    mintime = sheet.cell_value(COAST.index(minvalue) + 1, 0)
    avgcoast = sum(COAST)/float(len(COAST))
    
    data = {
            'maxtime': xlrd.xldate_as_tuple(maxtime, 0),
            'maxvalue': maxvalue,
            'mintime': xlrd.xldate_as_tuple(mintime, 0),
            'minvalue': minvalue,
            'avgcoast': avgcoast
    }
    return data

def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)

test()
