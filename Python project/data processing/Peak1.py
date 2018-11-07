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
#print zip(E,F)
r=zip(E,F)
#print r
# G=[]
G1=[]
G2=[]
for z in r:
    e1='s_time'
    e2='e_time'
    y1=e1,z[0]
    y2=e2,z[1]
    #print y1,y2
    G1.append(y1)
    G2.append(y2)
#print G1,G2
G11=[]
G12=[]
for d1 in G1:
    new_dict={}
    new_dict[d1[0]] = d1[1]
    G11.append(new_dict)
#print G11
    #print new_dict
for d2 in G2:
    ne_dict={}
    ne_dict[d2[0]] = d2[1]
    G12.append(ne_dict)
#print G12
    #print ne_dict
for d in range(len(G12)):
    for k in range(len(G11)):
        if d==k:
            #print G11[k],G12[d]
            d3=dict(G11[k],**G12[d])
            print d3
# d3=dict(G11.items()+G12.items())
# print d3
    # def foo(z,e):
    #     #return [(e,str(y)) for y in z]
    #     return [(e,str(z[0])
    # e='time'
    # a=foo(z,e)
    # print a
#     for b in a:
#         c=list(b)
#         #print c
#         new_dict={}
#         new_dict[c[0]] = c[1]
#         #print new_dict
#         # for f in range(len(new_dict)):
#         #     if f%2==0:
#         #         h=new_dict
#         #         print h
#         G.append(new_dict)
# #print G
# # for d in range(len(G)-1):
# #     #print G[d].items(),G[d+1].items()

# #     # d3=dict(G[d].items()+G[d+1].items())
# #     # print d3
# #     if d %2!=0:
# #         H=G[d]
# #         print H   
# #     else:
# #         I=G[d]
# #         print I
    
#     # # d3=dict(M,**N)
#     # # print d3

# # H=[]
# # for d in G:

# G1=G[0::2]  
# G2=G[1::2]
# #print G1,G2
# for d in range(len(G2)):
#     for k in range(len(G1)):
#         if d==k:
#             print G1[k],G2[d]
# #             # d3=dict(G1[k],**G2[d])
# #             # print d3


# # for d in range(len(G2)):
# #     G1[d].update(G2[d])
# # print G1

# # for d in range(len(G)):
# #     print G[d]






    


    
