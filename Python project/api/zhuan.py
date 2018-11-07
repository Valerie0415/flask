import datetime
import random
import time
import os
import csv
from csv import reader
import argparse
from influxdb import client as influxdb


db = influxdb.InfluxDBClient('192.168.0.130', 8086, 'root', '', database='test')

def read_data():
    with open('E:/Python project/data processing/product_2.csv') as f:
        return [x.split(',') for x in f.readlines()[1:]]

a = read_data()

for metric in a:
    influx_metric = [{
        'measurement': 'my',
        'time': metric[0],
        'fields': {
             'value': metric[1]
        }
    }]
    db.write_points(influx_metric)
# def read_data(filename):
#     with open(filename) as f:
#         reader = f.readlines()[1:]
#         for line in reader:
#             print line


# if __name__ == '__main__':
#     filename = 'E:/Python project/data processing/product_2.csv'
#     a = read_data(filename)