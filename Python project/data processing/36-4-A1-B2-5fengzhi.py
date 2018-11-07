#-*- coding: UTF-8 -*- 
import json
import time
import datetime
import matplotlib.pyplot as plt

#读取文件数据,并写入新的json文件
def loadFont():
	f = open(r"C:\Users\XuJie\Desktop\json\36-4-A1-B2-5.json", "r")       #不加r则会显示错误 
	data = json.load(f)             #data为读进来的所有数据
	C=[]              
	D=[]        
	D1=[]       
	for i1 in data['results']:
		C.append(i1['series'][0]['values'])
	for y1 in range(len(C)):
		for x1 in C[y1]:
			D.append(x1)
	D1.append(D)
	e='values'
	m=e,D1
	d=dict(zip(e,D1))
	n=d['v']
	# return len(n)            #n为新放的整个文件的数据 
	jsObj = json.dumps(d)  
	fileObject = open('C:\Users\XuJie\Desktop\json\json36-4-A1-B2-5.json', 'w')  
	fileObject.write(jsObj)  
	fileObject.close()  
	return

#读取新文件的json数据 
def loadFile():
	f1 = open(r"C:\Users\XuJie\Desktop\json\json36-4-A1-B2-5.json", "r")       #不加r则会显示错误 
	data1 = json.load(f1)
	value1 = data1['v']
	A=[]                        #A为时间戳存放列表
	B=[]                        #B为数据存放列表
	for y2 in range(len(value1)):
		A.append(value1[y2][0])
		B.append(value1[y2][1])
	# return len(A)
	da=[]
	dt=A[0]             #dt为时间戳的起始数据
	d1 = int(dt/1000000000)  
	return d1        

def loadFile1():
	f1 = open(r"C:\Users\XuJie\Desktop\json\json36-4-A1-B2-5.json", "r")       #不加r则会显示错误 
	data1 = json.load(f1)
	value1 = data1['v']
	A=[]                        #A为时间戳存放列表
	for y2 in range(len(value1)):
		A.append(value1[y2][0])
	return A

def loadFile2():
	f1 = open(r"C:\Users\XuJie\Desktop\json\json36-4-A1-B2-5.json", "r")       #不加r则会显示错误 
	data1 = json.load(f1)
	value1 = data1['v']
	B=[]                        #A为时间戳存放列表
	for y2 in range(len(value1)):
		B.append(value1[y2][1])
	return B

#时间戳转换函数,将每一天截取出来
def time1(y2):
	dateArray = datetime.datetime.utcfromtimestamp(y2)
	n=datetime.datetime(dateArray.year, dateArray.month, dateArray.day, 0, 0, 0)  #将时间格式化到当天凌晨
	# return n
	ti=[]
	for y3 in range(20):
		threeDayAgo = n + datetime.timedelta(days = y3)
		n1=(time.mktime(threeDayAgo.timetuple()))*1000000000
		ti.append(n1)
	return ti

#时间函数
def judgment(y4,y5):
	a1= [[] for i in range(len(y5))]
	for i1 in range(len(y4)):
		for i2 in range(len(y5)):
			if y5[i2]<=y4[i1] and y4[i1]<y5[i2+1]:
				a1[i2].append(y4[i1])
	return a1

def judgment1(y4,y5,y6):
	a2= [[] for j in range(len(y5))]
	# return a1
	for i1 in range(len(y4)):
		for i2 in range(len(y5)):
			if y5[i2]<=y4[i1] and y4[i1]<y5[i2+1]:
				a2[i2].append(y6[i1])
	return a2

t = loadFont()
t1 = loadFile() 
t2 = time1(t1)
t4 = loadFile1()
t5 = loadFile2()
t3 = judgment(t4,t2)
t6 = judgment1(t4,t2,t5)
# print t3
# print (t3[7])
print (t6[7])

# # # #画图显示
# # x1=range(0,len(ma_data))

plt.plot(t3[7],t6[7],label='36-4-A1-B2-5',color='blue')
plt.xlabel('temp')
plt.ylabel('values')
plt.title('current_c')
plt.legend()
plt.show()  
 
