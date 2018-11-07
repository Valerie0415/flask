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

#获取所有的数据点信息
class Data_Infor(Resource):
    def get(self):                                                                   
        (db,cursor)=connectdb()
        cursor.execute('select name,label,method,product_id from datapoints')
        datas = cursor.fetchall()        
        return jsonify({"datas":datas})
        closedb(db,cursor)

#获取某个产品的所有数据点信息
class Data_pro(Resource):
    def get(self,data_id):                                                                   
        (db,cursor)=connectdb()
        cursor.execute('select name,label,method,product_id from datapoints')
        datas = cursor.fetchall()
        data = filter(lambda t: t['product_id'] == data_id, datas)
        if len(data) == 0:
            abort(404)
        return jsonify({"data":data})
        closedb(db,cursor)       




api.add_resource(Data_Infor, '/v1/datapoint/:id')
api.add_resource(Data_pro, '/v1/datapoint/datapoint/<int:data_id>')


 
if __name__ == '__main__':
    app.run(debug = True)
     
