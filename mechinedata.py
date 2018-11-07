#-*- coding: UTF-8 -*- 
import psutil
import time
from influxdb import InfluxDBClient
cdata=psutil.cpu_times().user
data=psutil.net_io_counters().bytes_sent
free_used = psutil.virtual_memory().used 
free_total = psutil.virtual_memory().total
#内存利用率（已使用的内存/总内存）
percentage_free = (free_used * 1.0) / (free_total * 100)
io2=psutil.disk_io_counters().read_count
io1=psutil.disk_io_counters().write_count
json_body = [
                {
            "measurement": "datas",
            #"time": "2017-03-12T22:00:00Z",
            "fields": {
                "bytes_sent": data, 
                "percentage_free": percentage_free,
                "read_count": io2,
                "write_count": io1,
                "cpu_user": cdata
                    }
                }
            ]
    
client = InfluxDBClient('118.89.217.73',8086,'root','','mydb') # 初始化（指定要操作的数据库
client.write_points(json_body) # 写入数据，同时创建表

def showDBNames(client):
    result = client.query('select * from datas') # 显示数据库中的表
    print("Result: {0}".format(result))

showDBNames(client)
