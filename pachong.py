import requests
import random
import json
import time
import queue
import threading

# url = 'http://weike.enetedu.com/js_support.asp'
# vodid = '196783_4'
# xiangmu = '25'
# full_url = '%s?vodid=%s&xiangmu=%s&nxxx=%s' % (
#     url, vodid, xiangmu, random.random())
# print(full_url)
# resp = requests.get(full_url)
# print(resp.text)
TIMEOUT = 0.3
exitFlag = 0

threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue()
threads = []
threadID = 1


def dig_support(px):
    url = 'http://weike.enetedu.com/js_support.asp'
    vodid = '196783_5'
    xiangmu = '25'
    full_url = '%s?vodid=%s&xiangmu=%s&nxxx=%s' % (
        url, vodid, xiangmu, random.random())
    print(full_url)
    try:
        resp = requests.get(full_url, proxies=px, timeout=TIMEOUT)
        print(resp.text)
    except Exception as e:
        print('sth wrong with this proxy: %s' % px)
        print(e)

    # try:
    #     vodid = '174334_1'
    #     xiangmu = '25'
    #     full_url = '%s?vodid=%s&xiangmu=%s&nxxx=%s' % (
    #         url, vodid, xiangmu, random.random())
    #     resp = requests.get(full_url, proxies=px, timeout=TIMEOUT)
    #     print(resp.text)
    # except Exception as e:
    #     print('sth wrong with this proxy: %s' % px)
    #     print(e)


def dig_useradopt(px):
    url = 'http://weike.enetedu.com/js_useradopt.asp'
    vodid = '196783'
    xiangmu = '25'
    full_url = '%s?vodid=%s&xiangmu=%s&nzz=%s' % (
        url, vodid, xiangmu, random.random())
    print(full_url)
    try:
        resp = requests.get(full_url, proxies=px, timeout=TIMEOUT)
        print(resp.text)
    except Exception as e:
        print('sth wrong with this proxy: %s' % px)
        print(e)


def dig_share(px):
    url = 'http://weike.enetedu.com/js_share.asp'
    vodid = '196783'
    xiangmu = '25'
    full_url = '%s?vodid=%s&xiangmu=%s&nzz=%s' % (
        url, vodid, xiangmu, random.random())
    print(full_url)
    try:
        resp = requests.get(full_url, proxies=px, timeout=TIMEOUT)
        print(resp.text)
    except Exception as e:
        print('sth wrong with this proxy: %s' % px)
        print(e)


def get_proxy():
    resp = requests.get('http://localhost:8000')
    # print(resp.json())
    return resp.json()


def s():
    proxies = get_proxy()
    for proxy in proxies:
        if(proxy[2] > 5):
            p = 'http://%s:%s' % (proxy[0], proxy[1])
            # print(p)
            px = {'http': p}
            try:
                while 1:
                    pass
                    requests.get(
                        'http://weike.enetedu.com/play.asp?vodid=196783&e=25',
                        timeout=TIMEOUT)
                    # time.sleep(random.uniform(0, 1))
            except Exception:
                # print(e)
                pass
            dig_support(px)
            dig_useradopt(px)
            dig_share(px)


class myThread (threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        print("开启线程：")
        process_data(self, self.q)
        print("退出线程：")
        pass


def process_data(tid, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            proxy = q.get()

            p = 'http://%s:%s' % (proxy[0], proxy[1])
            # print(p)
            px = {'http': p}
            i = 0
            while i < 1000:

                try:
                    requests.get(
                        'http://weike.enetedu.com/play.asp?vodid=196783&e=25',
                        timeout=TIMEOUT, proxies=px)
                    # time.sleep(random.uniform(0, 1))
                except Exception:
                    # print(e)
                    pass

                dig_support(px)
                # dig_useradopt(px)
                dig_share(px)
                i += 1

            queueLock.release()
            print("Thread: %s\n %s" % (tid, proxy))
        else:
            queueLock.release()
        # time.sleep(1)

# while True:
#     # s()
#     print(time.time())
#     s()
#     time.sleep(random.uniform(0, 5))


def main():
    创建新线程
for i in range(10):
    thread = myThread(workQueue)
    thread.start()
    threads.append(thread)

# 填充队列
queueLock.acquire()
proxies = get_proxy()
for proxy in proxies:
    print(proxy)
    workQueue.put(proxy)
    print(workQueue)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")


# main()
#
# while 1:
#     px = {'http': '59.44.16.6:8000'}
#     dig_useradopt(px)
#     time.sleep(0.3)