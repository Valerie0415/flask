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

app = Flask(__name__)
api = Api(app)

def connectdb():
	db=MySQLdb.connect(host='192.0.0.125',port=3306,username='vagrant',passwd='vagrant', db='mydb')
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
        closedb(db,cursor)       

api.add_resource(Mac, '/v1/device/mac')

if __name__ == '__main__':
    app.run(debug = True)
     
