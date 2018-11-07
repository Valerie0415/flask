#-*- coding: UTF-8 -*- 
import psutil
import time
from influxdb import InfluxDBClient
p = psutil.Process(9896)
p1=p.num_threads()   #该进程包含的线程数量
# print p1
json_body = [
                {
            "measurement": "mypros",
            #"time": "2017-03-12T22:00:00Z",
            "fields": { 
                "num_threads": p1
                    }
                }
            ]
    
client = InfluxDBClient('118.89.217.73',8086,'root','','mydb') # 初始化（指定要操作的数据库
client.write_points(json_body) # 写入数据，同时创建表

def showDBNames(client):
    result = client.query('select * from mypros') # 显示数据库中的表
    print("Result: {0}".format(result))

showDBNames(client)
