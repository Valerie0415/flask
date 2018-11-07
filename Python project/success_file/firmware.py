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


class Firm_Info(Resource):
    def get(self):                                                                   
        (db,cursor)=connectdb()
        cursor.execute('select * from  firmwares')
        datas = cursor.fetchall()        
        return jsonify({"datas":datas})
        closedb(db,cursor)


class Firm_pro(Resource):
    def get(self,data_id):                                                                   
        (db,cursor)=connectdb()
        cursor.execute('select * from  firmwares')
        datas = cursor.fetchall()
        data = filter(lambda t: t['product_id'] == data_id, datas)
        if len(data) == 0:
            abort(404)
        return jsonify({"data":data})
        closedb(db,cursor)       


class Firm_dev(Resource):
    def get(self,data_id):
        (db,cursor)=connectdb()
        cursor.execute('select id,firmware_id from devices')
        datas = cursor.fetchall()        
        data = filter(lambda t: t['id'] == data_id, datas)
        if len(data) == 0:
            abort(404)
        return jsonify({'data': data})
        closedb(db,cursor)
 



api.add_resource(Firm_Info, '/v1/firmware/:id')
api.add_resource(Firm_pro, '/v1/firmware/product/<int:data_id>')
api.add_resource(Firm_dev,'/v1/firmware/device/<int:data_id>')

 
if __name__ == '__main__':
    app.run(debug = True)
     
