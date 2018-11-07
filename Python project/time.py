#-*- coding: UTF-8 -*- 
import json
import random
import numpy as np
import ch
ch.set_ch()
import matplotlib.mlab as mlab    
import matplotlib.pyplot as plt 
# import matplotlib as mpl
 
# mpl.rcParams['font.sans-serif'] = ['FangSong']
# mpl.rcParams['axes.unicode_minus']=False
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#ID3
A=[2.78,5.36,8.02,11.82,14.33]
#改进ID3
B=[1.95,2.99,4.98,7.32,9.97]

plt.figure(2)
x2=np.linspace(0,5000,5)   #从0到5000，总共5个点
plt.ylim()
plt.xlim(0,5000)
plt.plot(x2,A,'r--',label='预测值')
plt.plot(x2,B,color='blue',label='实际值')

# font1 = { 
#  'family' : 'NSimSun,Times New Roman',
# 'weight' : 'heavy',  
# # 'size'   : 15,  
# }  
# legend = plt.legend(handles=[A,B],prop=font1) 
plt.xlabel('样本数量')
plt.ylabel('运行时间(s)')
plt.title('运行时间对比')
plt.legend()
plt.grid(True, linestyle = "-.", color = "black", linewidth = "0.3")  
plt.show()
