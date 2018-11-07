#! /usr/bin/env python
#-*- coding:utf-8 -*-
from influxdb import InfluxDBClient
 
json_body = [
    {
        "measurement": "students",
        "tags": {
            "stuid": "s123"
        },
        #"time": "2017-03-12T22:00:00Z",
        "fields": {
            "score": 89
        }
    }
]
client = InfluxDBClient('192.168.0.130', 8086, 'root', '', 'test') # 初始化

result = client.query('select * from data')   
print("Result: {0}".format(result))
# def showDatas(client):
#         result = client.query('select * from students;')
#         print("Result: {0}".format(result))
 
# client = InfluxDBClient('192.168.0.130', 8086, 'root', '', 'test') # 初始化
# client.write_points(json_body) # 写入数据
# showDatas(client)  # 查询数据
# client.query('delete from students;') # 删除数据
# showDatas(client)  # 查询数据