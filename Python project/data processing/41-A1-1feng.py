#-*- coding: UTF-8 -*- 
import json
import time
import datetime
import matplotlib.pyplot as plt

#读取文件数据,并写入新的json文件
def loadFont():
	f = open(r"C:\Users\XuJie\Desktop\json\41-A1-1.json", "r")       #不加r则会显示错误 
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
	fileObject = open('C:\Users\XuJie\Desktop\json\json41-A1-1.json', 'w')  
	fileObject.write(jsObj)  
	fileObject.close()  
	return

#读取新文件的json数据 
def loadFile():
	f1 = open(r"C:\Users\XuJie\Desktop\json\json41-A1-1.json", "r")       #不加r则会显示错误 
	data1 = json.load(f1)
	value1 = data1['v']
	A=[]                        #A为时间戳存放列表
	B=[]                        #B为数据存放列表
	for y2 in range(len(value1)):
		A.append(value1[y2][0])
		B.append(value1[y2][1])
	# return len(A)
	da=[]
	dt=A[0]             #dt为所有时间戳的起始数据
	d1 = int(dt/1000000000)  
	return d1        

def loadFile1():
	f1 = open(r"C:\Users\XuJie\Desktop\json\json41-A1-1.json", "r")       #不加r则会显示错误 
	data1 = json.load(f1)
	value1 = data1['v']
	A=[]                        #A为时间戳存放列表
	for y2 in range(len(value1)):
		A.append(value1[y2][0])
	return A

def loadFile2():
	f1 = open(r"C:\Users\XuJie\Desktop\json\json41-A1-1.json", "r")       #不加r则会显示错误 
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
	for y3 in range(16):
		threeDayAgo = n + datetime.timedelta(days = y3)
		n1=(time.mktime(threeDayAgo.timetuple()))*1000000000
		ti.append(n1)
	return ti

#将时间函数，将时间戳按天切割，并存进列表里
def judgment(y4,y5):
	a1= [[] for i in range(len(y5))]
	for i1 in range(len(y4)):
		for i2 in range(len(y5)):
			if y5[i2]<=y4[i1] and y4[i1]<y5[i2+1]:
				a1[i2].append(y4[i1])
	return a1

#将时间戳对应的数值存进相同格式的列表里
def judgment1(y4,y5,y6):
	a2= [[] for j in range(len(y5))]
	# return a1
	for i1 in range(len(y4)):
		for i2 in range(len(y5)):
			if y5[i2]<=y4[i1] and y4[i1]<y5[i2+1]:
				a2[i2].append(y6[i1])
	return a2

#将每天的时间戳减去当天零点时间的时间戳
def initialTime(y7,y8):
	a= [[] for j1 in range(len(y8))]
	for i3 in range(len(y7)):
		for j2 in range(len(y8)):
			if i3==j2:
				for m in y7[i3]:
					m1=m-y8[j2]
					a[i3].append(m1)
	return a

t = loadFont()
t1 = loadFile() 
t2 = time1(t1)
t4 = loadFile1()
t5 = loadFile2()
t3 = judgment(t4,t2)
t6 = judgment1(t4,t2,t5)
# print t3
t7 = initialTime(t3,t2)
# print (t3[2])
print t7

# 画图显示

# plt.figure(1)#创建图表1  
plt.figure(1)#创建图表2  
ax1=plt.subplot(411)#在图表2中创建子图1  
ax2=plt.subplot(412)#在图表2中创建子图2 
ax3=plt.subplot(413)#在图表2中创建子图3 
ax4=plt.subplot(414)#在图表2中创建子图4 
plt.sca(ax1)  
plt.plot(t7[0],t6[0])  
plt.sca(ax2)  
plt.plot(t7[1],t6[1])  
plt.sca(ax3)  
plt.plot(t7[2],t6[2]) 
plt.sca(ax4)  
plt.plot(t7[3],t6[3])
plt.figure(2)#创建图表2  
ax11=plt.subplot(411)#在图表2中创建子图1  
ax21=plt.subplot(412)#在图表2中创建子图2 
ax31=plt.subplot(413)#在图表2中创建子图3 
ax41=plt.subplot(414)#在图表2中创建子图4
plt.sca(ax11)  
plt.plot(t7[4],t6[4])  
plt.sca(ax21)  
plt.plot(t7[5],t6[5])  
plt.sca(ax31)  
plt.plot(t7[6],t6[6]) 
plt.sca(ax41)  
plt.plot(t7[7],t6[7]) 

plt.figure(3)#创建图表3
ax12=plt.subplot(411)#在图表2中创建子图1  
ax22=plt.subplot(412)#在图表2中创建子图2 
ax32=plt.subplot(413)#在图表2中创建子图3 
ax42=plt.subplot(414)#在图表2中创建子图4
plt.sca(ax12)  
plt.plot(t7[8],t6[8])  
plt.sca(ax22)  
plt.plot(t7[9],t6[9])  
plt.sca(ax32)  
plt.plot(t7[10],t6[10]) 
plt.sca(ax42)  
plt.plot(t7[11],t6[11])

plt.figure(4)#创建图表4 
ax13=plt.subplot(411)#在图表2中创建子图1  
ax23=plt.subplot(412)#在图表2中创建子图2 
ax33=plt.subplot(413)#在图表2中创建子图3 
ax43=plt.subplot(414)#在图表2中创建子图4
plt.sca(ax13)  
plt.plot(t7[12],t6[12])  
plt.sca(ax23)  
plt.plot(t7[13],t6[13])  
plt.sca(ax33)  
plt.plot(t7[14],t6[14]) 
plt.sca(ax43)  
plt.plot(t7[15],t6[15]) 
plt.show()
