# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.

import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"
stations = []

def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    global stations
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    stations = sheet.row_values(0, start_colx=1, end_colx=9)
    stations = [str(a) for a in stations]
    data = {}

    for i in xrange(1, 9):
        region = sheet.col_values(i, start_rowx=1)
        maxval = max(region)
        maxtime = sheet.cell_value(region.index(maxval) + 1, 0)

        data[stations[i-1]] = [maxval, xlrd.xldate_as_tuple(maxtime, 0)]

    return data

def save_file(data, filename):
    with open(filename, 'wb') as csvfile:
        obj = csv.writer(csvfile, delimiter='|')
        obj.writerow(["Station", "Year", "Month", "Day", "Hour", "Max Load"])

        for i in xrange(8):
            time = data[stations[i]][1]
            row = [stations[i], time[0], time[1], time[2], time[3], data[stations[i]][0]]
            obj.writerow(row)

def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)

        
if __name__ == "__main__":
    test()

