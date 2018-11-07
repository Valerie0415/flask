#-*- coding: UTF-8 -*- 
import numpy as np
import matplotlib.pyplot as plt

def logsig(x):
    return 1/(1+np.exp(-x))

#建筑面积（m^2）
area=[30.08,4.535,51.023,3.965,6.602,78.603,5.092,3.465,50.224,51.264,11.232,35,11.618,24.5,26.515]
#地上层数
high=[30,7,28,12,6,52,4,6,15,18,6,15,9,25,7]
#建筑结构（砖混1、框剪2、剪力墙3）
structure=[2,4,5,1,4,3,4,3,4,3,5,3,5,5,1]
#地下层数
population=[1,3,1,0,0,3,1,0,2,1,0,2,1,1,0]
#施工日期
date=[410,220,570,180,273,900,270,330,450,900,300,450,220,560,340]
#建筑类型
roadarea=[1,3,1,2,1,1,3,1,1,1,2,1,2,1,1]

#用电量(单位：万吨)
energy=[66.73,50,66.73,86.2,89.5,643.5,84.84,200,435,456,300,73.56,369.5,401,418]

samplein = np.mat([area,high,structure,population,date,roadarea]) #3*20
sampleinminmax = np.array([samplein.min(axis=1).T.tolist()[0],samplein.max(axis=1).T.tolist()[0]]).transpose()#3*2，对应最大值最小值
sampleout = np.mat([energy])#2*20
sampleoutminmax = np.array([sampleout.min(axis=1).T.tolist()[0],sampleout.max(axis=1).T.tolist()[0]]).transpose()#2*2，对应最大值最小值

#3*20,20组数据
sampleinnorm = (2*(np.array(samplein.T)-sampleinminmax.transpose()[0])/(sampleinminmax.transpose()[1]-sampleinminmax.transpose()[0])-1).transpose()
#2*20
sampleoutnorm = (2*(np.array(sampleout.T).astype(float)-sampleoutminmax.transpose()[0])/(sampleoutminmax.transpose()[1]-sampleoutminmax.transpose()[0])-1).transpose()

#给输出样本添加噪音
noise = 0.03*np.random.rand(sampleoutnorm.shape[0],sampleoutnorm.shape[1])
sampleoutnorm += noise




maxepochs = 15000#最大迭代次数
learnrate = 0.035
errorfinal = 0.65*10**(-3)
samnum = 15
indim = 6
outdim = 1
hiddenunitnum = 13
#输入层到隐藏层的weight
w1 = 0.5*np.random.rand(hiddenunitnum,indim)-0.1
#隐藏层的b
b1 = 0.5*np.random.rand(hiddenunitnum,1)-0.1
#隐藏层到输出层的weight
w2 = 0.5*np.random.rand(outdim,hiddenunitnum)-0.1
#输出层的b
b2 = 0.5*np.random.rand(outdim,1)-0.1


errhistory = []

for i in range(maxepochs):
    hiddenout = logsig((np.dot(w1,sampleinnorm).transpose()+b1.transpose())).transpose()
    networkout = (np.dot(w2,hiddenout).transpose()+b2.transpose()).transpose()
    err = sampleoutnorm - networkout
    sse = sum(sum(err**2))

    errhistory.append(sse)
    if sse < errorfinal:
        break

    delta2 = err

    delta1 = np.dot(w2.transpose(),delta2)*hiddenout*(1-hiddenout)

    dw2 = np.dot(delta2,hiddenout.transpose())
    db2 = np.dot(delta2,np.ones((samnum,1)))

    dw1 = np.dot(delta1,sampleinnorm.transpose())
    db1 = np.dot(delta1,np.ones((samnum,1)))

    w2 += learnrate*dw2
    b2 += learnrate*db2

    w1 += learnrate*dw1
    b1 += learnrate*db1




# 误差曲线图
errhistory10 = np.log10(errhistory)
minerr = min(errhistory10)
plt.plot(errhistory10)
plt.plot(range(0,i+1000,1000),[minerr]*len(range(0,i+1000,1000)))

ax=plt.gca()
ax.set_yticks([-2,-1,0,1,2,minerr])
ax.set_yticklabels([u'$10^{-2}$',u'$10^{-1}$',u'$1$',u'$10^{1}$',u'$10^{2}$',str(('%.4f'%np.power(10,minerr)))])
ax.set_xlabel('iteration')
ax.set_ylabel('error')
ax.set_title('Error History')
plt.savefig('errorhistory5.png',dpi=700)
plt.close()


# 仿真输出和实际输出对比图
hiddenout = logsig((np.dot(w1,sampleinnorm).transpose()+b1.transpose())).transpose()
networkout = (np.dot(w2,hiddenout).transpose()+b2.transpose()).transpose()
diff = sampleoutminmax[:,1]-sampleoutminmax[:,0]
networkout2 = (networkout+1)/2
networkout2[0] = networkout2[0]*diff[0]+sampleoutminmax[0][0]
# networkout2[1] = networkout2[1]*diff[1]+sampleoutminmax[1][0]


print networkout2[0] #预测结果


sampleout = np.array(sampleout)

fig,axes = plt.subplots()
line1, =axes.plot(networkout2[0],'k',marker = u'$\circ$')
line2, = axes.plot(sampleout[0],'r',markeredgecolor='b',marker = u'$\star$',markersize=9)

axes.legend((line1,line2),('simulation output','real output'),loc = 'upper left')

yticks = [0,1000]
ytickslabel = [u'$0$',u'$1$']
axes.set_yticklabels(ytickslabel)
axes.set_ylabel(u'Electricity forecast$(10^3)$')

xticks = range(0,15,1)
xtickslabel = range(0,15,1)
axes.set_xticks(xticks)
axes.set_xticklabels(xtickslabel)
axes.set_xlabel(u'number')
axes.set_title('Electricity Forecast Simulation')


fig.savefig('simulation5.png',dpi=500,bbox_inches='tight')
plt.close()