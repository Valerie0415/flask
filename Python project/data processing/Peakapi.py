#-*- coding: UTF-8 -*- 
import re
from flask import abort
from flask import Flask
from flask import request
from flask import jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

class Mac(Resource):
    def get(self):
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
            if float(d[0])>=210:    #超过210为峰值数据
                C.append(d[1])
                D.append(m)
                pass
        # print C,D
        #print len(C)
        E=[]
        F=[]
        #将连续时间段的起始位置输出
        for n1 in range(len(D)):
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
                #print C[n2] ~12 
                pass
            else:
                #print C[n2]
                F.append(C[n2])
        # print F
        F.append(C[len(D)-1])
        #print F
        #print zip(E,F)
        w=zip(E,F)
        # return w
        G1=[]
        G2=[]
        for z in w:
            e1='f_time'
            e2='s_time'
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
        H=[]
        for d in range(len(G11)):
            for k in range(len(G12)):
                if d==k:
                    #print G11[k],G12[d]
                    d3=dict(G12[k],**G11[d])
                    #print d3
                    # return d3
                    H.append(d3)
        # return H,{'Access-Control-Allow-Origin':'*'}
        for x in H:
            #print x
            if x['f_time']==x['s_time']:
                H.remove(x)
        return H,{'Access-Control-Allow-Origin':'*'}


        # r=zip(E,F)
        # set={}
        # G=[]
        # for y in r:
        #     set.update({'12':y})
        #     #print set
        #     G.append(set)
        # return G

        # r=[]
        # dictionary=dict(zip(r,w))
        # return dictionary

api.add_resource(Mac, '/login')

if __name__ == '__main__':
    app.run(debug = True,port=8000,host='0.0.0.0')
     




    


    
