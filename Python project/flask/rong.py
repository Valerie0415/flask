#conding=utf-8
import time
#定义计数器
def get_counter(y):
    count=0
    for x in y:
    	if x==fail:
    		count=count+1		
    return count
counter = get_counter()

#关闭熔断器，每次失败调用时计数
class Closed():
	def get(self)
		if counter>50:
		    return Open()

#启动时钟，持续禁止访问
class Open():
	return error
	time.sleep(3)
	if counter<50:      #平均故障处理时间(3秒)	
		return Half_open()

#熔断状态,如果调用都成功（或一定比例）则认为恢复了，关闭熔断器
class Half_open():
	def get_request(self):
		if counter<50:
    		return Close()
    	else:
    		return Open()