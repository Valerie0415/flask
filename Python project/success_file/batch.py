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


class Information(Resource):
    def get(self):                                                                   
        (db,cursor)=connectdb()
        cursor.execute('select * from batchs')
        datas = cursor.fetchall()        
        return jsonify({"datas":datas})
        closedb(db,cursor)


class Pro_bat(Resource):
    def get(self,data_id):                                                                   
        (db,cursor)=connectdb()
        cursor.execute('select * from product_batches')
        datas = cursor.fetchall()
        data = filter(lambda t: t['product_id'] == data_id, datas)
        if len(data) == 0:
            abort(404)
        return jsonify({"data":data})
        closedb(db,cursor)       


class Dev_bat(Resource):
    def get(self,data_id):
        (db,cursor)=connectdb()
        cursor.execute('select id,batch_id from devices')
        
        datas = cursor.fetchall()        
        data = filter(lambda t: t['id'] == data_id, datas)
        if len(data) == 0:
            abort(404)
        return jsonify({'data': data})
        closedb(db,cursor)
 



api.add_resource(Information, '/v1/batch/:id')
api.add_resource(Pro_bat, '/v1/batch/product/<int:data_id>')
api.add_resource(Dev_bat,'/v1/batch/device/<int:data_id>')

 
if __name__ == '__main__':
    app.run(debug = True)
     
