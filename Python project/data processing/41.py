#-*- coding: UTF-8 -*- 
import json
import random
import matplotlib.mlab as mlab    
import matplotlib.pyplot as plt                                                                    

#判断不同区间数量
def shuju(x):
	n=[random.randint(0,x) for i in range(31)]
	return n
def Interval(y,y1,y2):
	r= [[] for j in range(len(y2)+1)]
	m1=[0]                                                                                                                                   
	m2=m1+y2
	m2.append(1)
	# return m2
	x=len(m2)
	if i+1<=x:
		for i in m2:
			for j in y:
				if j>=m2[i] and j<y1*m2[i]
					r[i] +=1

t=shuju(315)
t1 = Interval(t,2,[0.2,0.5])
print (t1)

# # 画饼图显示
# labels=['0-10%','10%-20%','20%-30%','30%-40%','40%-50%','50%-60%','60%-70%','70%-80%','80%-90%','90%-100%']  
# # X=t7    
  
# fig = plt.figure()  
# plt.pie(t7,labels=labels,autopct='%1.2f%%') #画饼图（数据，数据对应的标签，百分数保留两位小数点）  
# plt.title("41-A1-1 Pie chart")
# plt.show()    
# # plt.savefig("PieChart1.jpg")
