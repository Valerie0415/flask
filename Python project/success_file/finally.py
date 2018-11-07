import json
import MySQLdb
import datetime
from flask import abort
from flask import Flask
from flask import request
from flask import jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse
# from flask.ext.restful import reqparse, abort, Api, Resource
# import MySQLdb.cursors


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
        cursor.execute('select * from devices')
        datas = cursor.fetchall()
        
        return jsonify({"datas":datas})
        closedb(db,cursor)

class Mac(Resource):
    def get(self):                                                                   
        (db,cursor)=connectdb()
        cursor.execute('select mac,product_id from devices')
        datas = cursor.fetchall()
        return jsonify({"datas":datas})
        closedb(db,cursor)       


class Form(Resource):
    def get(self,data_id):
        (db,cursor)=connectdb()
        cursor.execute('select * from devices')
        datas = cursor.fetchall()
        
        data = filter(lambda t: t['ID'] == data_id, datas)
        if len(data) == 0:
            abort(404)
        return jsonify({'data': data[0]})
        closedb(db,cursor)
    
    

api.add_resource(FormList, '/v1/device')
api.add_resource(Mac, '/v1/device/mac')
api.add_resource(Form,'/v1/device/<int:data_id>')

 
if __name__ == '__main__':
     app.run(debug = True,port=2000)
     
