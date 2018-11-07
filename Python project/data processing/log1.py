#-*- coding: UTF-8 -*- 
import re
#f = codecs.open("E:\Python project\suju\data.txt","r","utf-8")
f = open("E:\Python project\data processing\data4.txt","r")
lines = f.readlines()
A=[]
# B=[]
for line in lines:
    s= re.split("\n|\t",line)
    #print s
    r=s[0:2]
    #print r

    r1=float(r[1].replace('.','.'))
    #print r1,r[0]

    A.append(r1)
    A.append(r[0])
#print A
B=[]
for i in range(len(A)):
    if i%2==0:
        x=A[i:i+2]
        #print x
        B.append(x)
#print B
#输出峰值数据产生的时间，每个都输出-
for m in B:
    if m[0]>=210:
        print m[1]
# for m in B:
#     print B
    # for n in x1:
    #     print n
        # if n[0]>=210:
        #     print n[1]



    


    
