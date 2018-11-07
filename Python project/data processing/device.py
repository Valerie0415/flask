#-*- coding: UTF-8 -*- 
import json
import MySQLdb
import datetime
import re
from flask.ext import restful
from flask import abort,Flask,request,jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = restful.Api(app)

def connectdb():
	db=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='mydb',port=3306)
	cursor=db.cursor(cursorclass = MySQLdb.cursors.DictCursor)
	return (db,cursor)
      
def closedb():
	db.close()
	cursor.close()

class Mac(Resource):
    def get(self):                                                                   
        (db,cursor)=connectdb()
        cursor.execute('select id,mac,product_id from devices')
        datas = cursor.fetchall()
        return jsonify({'code':'200','message':'OK',"datas":datas})
        

class Serie(Resource):
    def get(self,data_id):
        (db,cursor)=connectdb()
        cursor.execute('select * from devices')       
        datas = cursor.fetchall()
        #a=[]
        a=data_id[0:]
        b=[]
        #a.append(data_id)
        r=re.split(",",a)
        for i in r:   
            data = filter(lambda t: t['mac'] == i, datas)
            if len(data) == 0:
                abort(404)
            #return jsonify({'data': data})
            b.append(data)
        return jsonify(b)

class Sur(Resource):
    def get(self,data_id):
        (db,cursor)=connectdb()
        cursor.execute('select * from devices')       
        datas = cursor.fetchall()
        b=[]
        r=data_id.split(",")
        for i in r:   
            data = filter(lambda t: t['mac'] == i, datas)
            if len(data) == 0:
                abort(404)
            b.append(data)
        return jsonify(b)

class Sea(Resource):
    def get(self,data_id):
        (db,cursor)=connectdb()
        cursor.execute('select * from devices')       
        datas = cursor.fetchall()
        r=data_id.split(",")
        b=[]
        for i in r:
            try:
                m=int(i)
                b.append(m)
            except Exception:
                return error
        a=[]
        for y in b:
            data = filter(lambda t: t['id'] == y, datas)
            if len(data) == 0:
                abort(404)
            a.append(data)
        return jsonify(a)

api.add_resource(Mac, '/v1/device/mac')
api.add_resource(Serie,'/v1/test/<string:data_id>')
api.add_resource(Sur,'/v1/<string:data_id>')
api.add_resource(Sea,'/v1/text/<string:data_id>')

if __name__ == '__main__':
    app.run(debug = True)
     
