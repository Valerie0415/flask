#-*- coding: UTF-8 -*- 
import re
import json
import time
import datetime
import matplotlib.pyplot as plt
f = open(r"C:\Users\XuJie\Desktop\json\1.json", "r")       #不加第一个r则会显示错误 
data = json.load(f)
#return data
value = data['results'][0]['series'][0]['values']          #注意列表里数据的读取
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
#print B
sum = 0
result = list( 0 for x in B)

for i in range( 0, 200):
	sum = sum + B[i]
	result[i] = sum / (i+1)

for i in range( 200, len(B) ):
	sum = sum - B[i-200] + B[i]
	result[i] = sum / 200

print result
# D=[]
# for z in range(4):
# 	for y in range(len(B)):
# 		if (y+z)<len(B):
# 			m=(B[y]+B[y+z])/(z+2)
# 		D.append(m)
# print D
# print len(D)

# for y in range(len(B)):
# 	for z in range(4):
# 		pass
# 	if (y+z)<len(B):
# 		m=(B[y]+B[y+z])/(z+2)
# 		D.append(m)
# 		# m=(B[y]+B[y+1]+B[y+2]+B[y+3]+B[y+4]+B[y+5]+B[y+6]+B[y+7]+B[y+8]+B[y+9])/10
# 		# D.append(m)
# print D
# print len(D)

# 	for z in range(20):
# 		pass
# 	# m=(B[len(B)-y]+B[len(B)-y-z])/(z+1)
# 	if (y+z)<len((B)):
# 		m=(B[y]+B[y+z])/(z+1)
# 		D.append(m)
# # print len(D)
# print len(D)
x1=range(0,len(result))
plt.plot(x1,result,label='Mean value',color='blue')
# x2=range(0,len(A))
# plt.plot(x2,B,label='Initial value',color='red')
plt.xlabel('row')
plt.ylabel('values')
plt.title('current_c')
plt.legend()
plt.show()  



