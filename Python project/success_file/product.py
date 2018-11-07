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


class ID(Resource):
    def get(self):                                                                   
        (db,cursor)=connectdb()
        cursor.execute('select * from products')
        datas = cursor.fetchall()        
        return jsonify({"datas":datas})
        closedb(db,cursor)


class Model(Resource):
    def get(self,data_id):                                                                   
        (db,cursor)=connectdb()
        cursor.execute('select id,model,created from products')
        datas = cursor.fetchall()
        data = filter(lambda t: t['model'] == data_id, datas)
        if len(data) == 0:
            abort(404)
        return jsonify({"datas":datas})
        closedb(db,cursor)       


class Serie(Resource):
    def get(self,data_id):
        (db,cursor)=connectdb()
        cursor.execute('select * from product_series')
        
        datas = cursor.fetchall()        
        data = filter(lambda t: t['id'] == data_id, datas)
        if len(data) == 0:
            abort(404)
        return jsonify({'data': data})
        closedb(db,cursor)
 

class User_dev(Resource):
    def get(self,data_id):
        (db,cursor)=connectdb()
        cursor.execute('select id,creator from products')
        datas = cursor.fetchall()        
        data = filter(lambda t: t['creator'] == data_id, datas)
        if len(data) == 0:
            abort(404)
        return jsonify({'data': data})
        closedb(db,cursor)
 
class User_devser(Resource):
    def get(self,data_id):
        (db,cursor)=connectdb()
        cursor.execute('select serie_id,creator from products')
        datas = cursor.fetchall()        
        data = filter(lambda t: t['creator'] == data_id, datas)
        if len(data) == 0:
            abort(404)
        return jsonify({'data': data})
        closedb(db,cursor)


api.add_resource(ID, '/v1/products/:id')
api.add_resource(Model, '/v1/product/model/<string:data_id>')
api.add_resource(Serie,'/v1/product/serie/<int:data_id>/products')
api.add_resource(User_dev,'/v1/product/user/<int:data_id>/products')
api.add_resource(User_devser,'/v1/user/<int:data_id>/series')

 
if __name__ == '__main__':
    app.run(debug = True)
     
