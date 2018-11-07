#-*- coding: UTF-8 -*- 
import re
f = open("E:\Python project\data processing\data4.txt","r")
lines = f.readlines()
A=[]
for line in lines:
    s= re.split("\n|\t",line)
    #print s
    r=s[0:2]
    #print r
    A.append(r[1])
    A.append(r[0])
#print A
B=[]
for i in range(len(A)):
    if i%2==0:
        x=A[i:i+2]
        #print x
        B.append(x)
#print B
#输出峰值数据产生的时间，循环输出每个结果
# for m in B:
#     if float(m[0])>=210:
#         print m[1]
#输出峰值数据产生的时间，将其时间放进一个列表中
# C=[]
# for m in range(len(B)-1):   #按照索引将数值遍历出来
#     d=B[m]
#     if float(d[0])>=210:
#         C.append(d[1])
#         pass
# print C
C=[]
D=[]
for m in range(len(B)-1):   #按照索引将数值遍历出来
    d=B[m]
    if float(d[0])>=210:
        C.append(d[1])
        D.append(m)
        pass
# print C,D
#print len(C)
E=[]
F=[]
#将连续时间段的起始位置输出
for n1 in range(len(D)):
    #print n1
    #print D[n1]
    if D[n1]-D[n1-1]==1:
        #print C[n1]
        pass
    else:
        #print C[n1]
        E.append(C[n1])
#print E
#将连续时间段的终止位置输出
for n2 in range(len(D)-1):
    if D[n2+1]-D[n2]==1:
        #print C[n2]
        pass
    else:
        #print C[n2]
        F.append(C[n2])
# print F
F.append(C[len(D)-1])
#print F
print zip(E,F)





    


    
