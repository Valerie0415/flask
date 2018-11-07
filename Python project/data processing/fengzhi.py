#-*- coding: UTF-8 -*- 
import json
import time
import datetime
import matplotlib.pyplot as plt

#读取文件数据
def loadFont():
	f = open(r"C:\Users\XuJie\Desktop\json\27-4-A1-4.json", "r")       #不加r则会显示错误 
	data = json.load(f)
	#return data
	value = data['results'][0]['series'][0]['values']          #注意列表里数据的读取
	A=[]
	B=[]

	for y in value:
		x = time.localtime(int(y[0]/1000000000))
		d = time.strftime("%Y-%m-%d %H:%M:%S",x)
		A.append(d)
		B.append(y[1])
	return B
def loadFont1():
	f = open(r"C:\Users\XuJie\Desktop\json\27-4-A1-4.json", "r")       #不加r则会显示错误 
	data1 = json.load(f)
	#return data
	value1 = data1['results'][0]['series'][0]['values']          #注意列表里数据的读取
	A=[]
	m=0
	for y1 in value1:
		m+=1
		if m == 10000:

			x1 = time.localtime(int(y1[0]/1000000000))
			d1 = time.strftime("%Y-%m-%d %H:%M:%S",x1)
			A.append(d1)
			m = 0
		else:
			A.append(None)
	return A

#滑动平均每隔200求一次平均值
def moving_average(l, N):
	sum = 0
	result = list( 0 for x in l)
 
	for i in range( 0, N ):
		sum=sum+l[i]
		result[i]=sum/(i+1)
 
	for y in range(N,len(l)):
		sum=sum-l[y-N]+l[y]
		result[y]=sum/N
 
	return result

t = loadFont() 
t1 = loadFont1()
ma_data = moving_average(t, 200)
print(t1)
#print(ma_data)


fig, ax = plt.subplots(1,1) 
ax.plot(range(len(t1)),ma_data)
ax.set_xticks(range(len(t1)))
ax.set_xticklabels(t1, rotation='vertical', fontsize=10)
plt.show()

#画图显示
# x1=range(0,len(ma_data))
# plt.plot(x1,ma_data,label='Mean value',color='blue')
# plt.xlabel('row')
# plt.ylabel('values')
# plt.title('current_c')
# plt.legend()
# plt.show()  
 
