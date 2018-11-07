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

def showDatas(client):
        result = client.query('select * from students')
        print("Result: {0}".format(result))

client = InfluxDBClient('118.89.217.73', 8086, 'root', '', 'testdb1') # 初始化

client.write_points(json_body) # 写入数据
showDatas(client)  # 查询数据
print client.get_list_database() # 显示所有数据库名称
# client.query('delete from students') # 删除数据
# showDatas(client)  # 查询数据


