#-*- coding: UTF-8 -*- 
import re
import matplotlib.pyplot as plt

f = open("E:\Python project\log.txt","r")
#读取文件并将其分割
lines = f.readlines()
rows = len(lines)  #将文件的总行数计算出来
#print rows
Y1=[]
Y2=[]
Y3=[]
Y4=[]
Y5=[]
for line in lines:
    r=line[11:-2]
    s= re.split(": |, ",r) #此时转换出来为字符串列表
    #print s
    key=s[0::2]  #将其字符串列表每隔一个数取一次值，将其ID和数据量分开两个列表存放
    value=s[1::2]
    #print key,value
    A=['121','122','123','124','128'] #判断ID是否存在在列表A中，若不存在则往列表b里面添ID，列表a里面补0
    for x in A:
    	if x in key:
    		pass
    	else:
    		key.append(x)
    		value.append('0')
    		pass             
    #print key,value    #跳出循环，不然每次循环的数值都会取到		
    dictionary=dict(zip(key,value))  #将列表转化成字典对应取值
    #print dictionary
    d1=dictionary['121']
    d2=dictionary['122']
    d3=dictionary['123']
    d4=dictionary['124']
    d5=dictionary['128']

   
    #将数据放进同一个列表中
    Y1.append(d1)
    Y2.append(d2)
    Y3.append(d3)
    Y4.append(d4)
    Y5.append(d5)


#print Y1
print map(int,Y1)
print map(int,Y2)
print map(int,Y3)
print map(int,Y4)
print map(int,Y5)
x1=range(0,rows)
x2=range(0,rows)
x3=range(0,rows)
x4=range(0,rows)
x5=range(0,rows)
plt.plot(x1,Y1,label='id=121',color='red')
plt.plot(x2,Y2,label='id=122',color='green')
plt.plot(x3,Y3,label='id=123',color='black')
plt.plot(x4,Y4,label='id=124',color='yellow')
plt.plot(x5,Y5,label='id=128',color='cyan')
plt.xlabel('row')
plt.ylabel('values')
plt.title('device data')
plt.legend()
plt.show()    
