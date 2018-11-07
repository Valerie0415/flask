# coding:UTF-8
import csv
import re
f=open('E:\Python project\data processing\product_2.csv','r')
lines=f.readlines()
f.close()

sts=[]
for line in lines:
	sts.append(line.split(','))
Y1=[]
for st in sts:
	A=[st[1]]
	B=[st[5]]
	#print A,B                
	dictionary=dict(zip(B,A))
	#print dictionary         #打印出device和time组合的字典
	for k in dictionary.keys():		
		if k=='11':
		 	d1=dictionary.values()
		 	#print d1
		 	Y1.append(d1)
		 	pass
#print Y1
t1=[]
[t1.extend(i) for i in Y1]
r1=map(int,t1)   #将str转换成int类型
#print r1
D=[]
for m in range(len(r1)-1):   #按照索引将数值遍历出来
	d=r1[m+1]-r1[m]
	D.append(d)          #按照索引取值
# print D
# rows = len(D)  #将文件的总行数计算出来
# print rows
r11=D[3:-1]
#print r11
r12=[]
for n in r11:
	if len(str(n))<11:
		r12.append(n)
		pass
#print r12
r13=[]
for x1 in r12:
	y=(x1-5600000000.0)/56000000.0
	r13.append(y)
#print r13
x121=[]
x122=[]
x123=[]
x124=[]
x125=[]
x126=[]
x127=[]
x128=[]
x129=[]
x120=[]
x130=[]

row1=None
row2=None
row3=None
row4=None
row5=None
row6=None
row7=None
row8=None
row9=None
row0=None
rows=None
for x12 in r13:
	if x12>=0 and x12<=10:
		x121.append(x12)
		row1 = len(x121)
		pass
	elif x12>10 and x12<=20:
		x122.append(x12)
		row2 = len(x122)
		pass
	elif x12>20 and x12<=30:
		x123.append(x12)
		row3 = len(x123)
		pass
	elif x12>30 and x12<=40:
		x124.append(x12)
		row4 = len(x124)
		pass
	elif x12>40 and x12<=50:
		x125.append(x12)
		row5 = len(x125)
		pass
	elif x12>50 and x12<=60:
		x126.append(x12)
		row6 = len(x126)
		pass
	elif x12>60 and x12<=70:
		x127.append(x12)
		row7 = len(x127)
		pass
	elif x12>70 and x12<=80:
		x128.append(x12)
		row8 = len(x128)
		pass
	elif (x12>80 and x12<=90)==1:
		x129.append(x12)
		row9 =len(x129)
		pass
	elif x12>90 and x12<=100:
		x120.append(x12)
		row0 = len(x120)
		pass
	else:
		x130.append(x12)
		rows = len(x130)
		pass
print row1,row2,row3,row4,row5,row6,row7,row8,row9,row0,rows

