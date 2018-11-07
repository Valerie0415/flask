#-*- coding: UTF-8 -*- 
import json
import time
import datetime
import matplotlib.pyplot as plt
f = open(r"C:\Users\XuJie\Desktop\json\44-4-A1-2.json", "r")       #不加第一个r则会显示错误 
data = json.load(f)
#return data
value = data['results'][0]['series'][0]['values']   
print(len(value))       #注意列表里数据的读取
A=[]
B=[]
for i in value:
	x = time.localtime(int(i[0]/1000000000))
	d = time.strftime("%Y-%m-%d %H:%M:%S",x)
	A.append(d)
	B.append(i[1])
	# C=dict(zip(A,B))
C=zip(A,B)
# print A,B,len(A),len(B)
# print len(B)
sum = 0
result = list( 0 for x in B)

for i in range( 0, 400):
	sum = sum + B[i]
	result[i] = sum / (i+1)

for i in range( 400, len(B) ):
	sum = sum - B[i-400] + B[i]
	result[i] = sum / 400

print result

x1=range(0,len(result))
plt.plot(x1,result,label='Mean value',color='blue')
# x2=range(0,len(A))
# plt.plot(x2,B,label='Initial value',color='red')
plt.xlabel('row')
plt.ylabel('values')
plt.title('current_c')
plt.legend()
plt.show()  



