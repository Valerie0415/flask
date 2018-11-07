#! /usr/bin/env python
#-*- coding:utf-8 -*-
# import redis    # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

# pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
# r = redis.Redis(connection_pool=pool)
# r.set('gender', 'male')     # key是"gender" value是"male" 将键值对存入redis缓存
# print(r.get('gender'))      # gender 取出键male对应的值
#coding=utf-8
import psutil
import sys
import time
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
            cpu = int(cpupercent / cpucount)
            if cpu <= 50:
                print u'CPU使用率:%s%%' % cpu + '         ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                print>> text, u'CPU使用率:%s%%' % cpu + '         ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            else:
                print u'CPU使用率:%s%%,占用率过高' % cpu + '         ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                print>> text, u'CPU使用率:%s%%,占用率过高' % cpu + '         ' + time.strftime('%Y-%m-%d %H:%M:%S',
                                                                                       time.localtime())
        text.close()
    print u'进程%s的' % PID + u'cpu监控已经运行，结果将在result.txt生成'
    time.sleep(1)
    print "-------------------------------------------------"
    print get_cpu_info()
finally:
    print  u'进程%s' % PID + u'已经结束'
    raw_input()

