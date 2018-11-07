#! /usr/bin/env python
#-*- coding:utf-8 -*-
import psutil
import sys
import time
from influxdb import InfluxDBClient
try:
    #输入需要监测的进程PID
    PID = raw_input('ProcessPID:')
    def get_cpu_info():
        reload(sys)
        sys.setdefaultencoding('utf-8')
        #将结果记录到本地文本
        text = open('CPUresult.txt', 'w')
        i = 0
        #现实循环
        while i < 100000000000000:
            i = i + 1
            #找出本机CPU的逻辑核个数
            cpucount = psutil.cpu_count(logical=True)
            #传入进程PID，实现监测功能
            process = psutil.Process(int(PID))
            cpupercent = process.cpu_percent(interval=2)
            #得到进程CPU占用，同资源检测管理器的数据
            cpu = cpupercent / cpucount
            # return cpu
            return cpu
        text.close()
    print u'进程%s的' % PID + u'cpu监控已经运行，结果将在result.txt生成'
    time.sleep(1)
    print "-------------------------------------------------"
    print get_cpu_info()
    json_body = [
                {
            "measurement": "cpu",
            "tags": {
                "stuid": "s123"
            },
            #"time": "2017-03-12T22:00:00Z",
            "fields": {
                "score": get_cpu_info()
                    }
                }
            ]
    
    client = InfluxDBClient('118.89.217.73',8086,'root','','collectd') # 初始化（指定要操作的数据库
    client.write_points(json_body) # 写入数据，同时创建表
    
    def showDBNames(client):
        result = client.query('select * from cpu') # 显示数据库中的表
        print("Result: {0}".format(result))
    
    showDBNames(client)
finally:
    print  u'进程%s' % PID + u'已经结束'
    raw_input()