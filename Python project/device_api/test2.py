#-*- coding: UTF-8 -*- 
import json
import MySQLdb
import datetime
from flask import abort
from flask import Flask
from flask import request
from flask import jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import make_response


app = Flask(__name__)
api = Api(app)


def connectdb():
	db=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='mydb',port=3306)
	cursor=db.cursor(cursorclass = MySQLdb.cursors.DictCursor)
	return (db,cursor)
      

def closedb():
	db.close()
	cursor.close()

class FormList(Resource):
    def get(self):                                                                   
        (db,cursor)=connectdb()
        cursor.execute('select * from devices limit 2,4')
        datas = cursor.fetchall()        
        return jsonify({'code':'200','message':'OK','datas': datas})
        closedb(db,cursor)


class Form(Resource):

    def get(self,data_id):
        (db,cursor)=connectdb()        
        cursor.execute('select * from devices')
        datas = cursor.fetchall()        
        data = filter(lambda t: t['id'] == data_id, datas)  
        if not data:                
        #if len(data) == 0:  #若数据库数据为空  
            return jsonify({'code':'1001','message':'uri_not_found'}) 
        return jsonify({'code':'200','message':'OK','data': data})    
        closedb(db,cursor)




api.add_resource(FormList, '/v1/device/:id')
api.add_resource(Form,'/v1/device/<int:data_id>')

 
if __name__ == '__main__':
    app.run(debug = True,port=8000)
     
