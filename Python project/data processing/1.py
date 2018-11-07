#-*- coding: UTF-8 -*- 
import json
import random
import ch
ch.set_ch()
import matplotlib.mlab as mlab    
import matplotlib.pyplot as plt 
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# plt.rcParams['font.sas-serig']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号    
# for i in range(len(A)):
# 	for j in range(len(B)):
# 		if n==A[i] and i==j:
# 			print B[j]

#B为实际值
B=[66.73,50,66.73,86.2,89.5,439.5,84.84,200.0,435,456,300,73.56,369.5,401,418]
A=[68.79,52.3,67.9,88.4,93.5,448.8,80.31,208.2,428.9,448.0,312.2,70.7,358.2,410.5,406.3]
#A为仿真值
#A=[70.87,45.32,70.82,80.2,88.3,425.8,80.84,190,410.0,470.0,329.0,69.56,346.5,371.0,440.0]
D=[]   #相对误差值
E=[]
C1=[]   #误差值
for i in range(len(A)):
	C=A[i]-B[i]    #误差图
	C1.append(C)
	c=abs(C)        #绝对误差
	d=c/B[i]        #相对误差
	D.append(d)
print D
s=0
s1=0
for x in range(len(D)):
	s=s+D[x]
	s1=s/len(D)  #平均相对误差
print s1
plt.figure(1)
x2=range(len(D))
plt.plot(x2,D,color='red')
plt.xlabel('工地编号')
plt.ylabel('相对误差')
plt.title('相对误差曲线')
plt.legend()

plt.figure(2)
x2=range(len(C1))
plt.plot(x2,A,'r--',label='预测值')
plt.plot(x2,B,color='blue',label='实际值')
plt.xlabel('工地编号')
plt.ylabel('负荷值')
plt.title('负荷仿真曲线')
plt.legend()
plt.grid(True, linestyle = "-.", color = "black", linewidth = "0.3")  
plt.show()
