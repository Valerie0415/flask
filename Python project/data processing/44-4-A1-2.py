#-*- coding: UTF-8 -*- 
import json
import time
import datetime
import matplotlib.pyplot as plt

#读取文件数据
def loadFont():
	f = open(r"C:\Users\XuJie\Desktop\json\44-4-A1-2.json", "r")       #不加r则会显示错误 
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

#滑动平均每隔N条数据求一次平均值
def moving_average(l, N):
	sum = 0
	result = list( 0 for x in l)

	for i in range( 0, N ):
		sum=sum+l[i]
		result[i]=sum/(i+1)
 
	for z in range(N,len(l)):
		sum=sum-l[z-N]+l[z]
		result[z]=sum/N
 
	return result

t = loadFont() 
ma_data = moving_average(t, 180)
print(len(t))
#print(ma_data)

#画图显示
x1=range(0,len(ma_data))
plt.plot(x1,ma_data,label='30 Mean value',color='blue')

# x2=range(0,len(t))
# plt.plot(x2,t,label='Initial value',color='red')

plt.xlabel('row')
plt.ylabel('values')
plt.title('44-4-A1-2 current_c')
plt.legend()
plt.show()  
 
