#-*- coding: UTF-8 -*- 
import json
import time
import datetime
import matplotlib.mlab as mlab    
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
	n=d['v']                  #n为新放的整个文件的数据       
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
	dt=A[0]                    #dt为时间戳的起始数据
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
	for y3 in range(20):
		threeDayAgo = n + datetime.timedelta(days = y3)
		n1=(time.mktime(threeDayAgo.timetuple()))*1000000000
		ti.append(n1)
	return ti

#时间函数，将时间戳按天切割，并存进列表里
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
	return a2[3]


#判断不同区间数量
def Interval(y7):
	a= []
	a1= [[] for j in range(9)]
	r=0
	r1=0
	r2=0
	r3=0
	r4=0
	r5=0
	r6=0
	r7=0
	r8=0
	r9=0
	for j in y7:
		if j>=0 and j<315*0.1:
			a1[0].append(j)
			r=len(a1[0])
		elif j>=315*0.1 and j<315*0.2:
			a1[1].append(j)
			r1=len(a1[1])
		elif j>=315*0.2 and j<315*0.3:
			a1[2].append(j)
			r2=len(a1[2])
		elif j>=315*0.3 and j<315*0.4:
			a1[3].append(j)
			r3=len(a1[3])
		elif j>=315*0.4 and j<315*0.5:
			a1[4].append(j)
			r4=len(a1[4])
		elif j>=315*0.5 and j<315*0.6:
			a1[5].append(j)
			r5=len(a1[5])
		elif j>=315*0.6 and j<315*0.7:
			a1[6].append(j)
			r6=len(a1[6])
		elif j>=315*0.7 and j<315*0.8:
			a1[7].append(j)
			r7=len(a1[7])
		elif j>=315*0.8 and j<315*0.9:
			a1[8].append(j)
			r8=len(a1[8])
		else:
			a1[9].append(j)
			r9=len(a1[9])
	a.append(r)
	a.append(r1)
	a.append(r2)
	a.append(r3)
	a.append(r4)
	a.append(r5)
	a.append(r6)
	a.append(r7)
	a.append(r8)
	a.append(r9)
	return a


t = loadFont()
t1 = loadFile() 
t2 = time1(t1)
t4 = loadFile1()
t5 = loadFile2()
t3 = judgment(t4,t2)
t6 = judgment1(t4,t2,t5)
t7 = Interval(t6)
print (t7)

# 画饼图显示
labels=['0-10%','10%-20%','20%-30%','30%-40%','40%-50%','50%-60%','60%-70%','70%-80%','80%-90%','90%-100%']  
# X=t7    
  
fig = plt.figure()  
plt.pie(t7,labels=labels,autopct='%1.2f%%') #画饼图（数据，数据对应的标签，百分数保留两位小数点）  
plt.title("41-A1-1 Pie chart")
plt.show()    
# plt.savefig("PieChart1.jpg")