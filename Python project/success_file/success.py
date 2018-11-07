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
	db=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='mydb',port=3306)
	cursor=db.cursor(cursorclass = MySQLdb.cursors.DictCursor)
	return (db,cursor)


def closedb():
	db.close()
	cursor.close()


class TodoList(Resource):
    def get(self):                                                                   
        (db,cursor)=connectdb()
        cursor.execute('select * from devices')
        datas = cursor.fetchall()
        
        return jsonify({"datas":datas})
        closedb(db,cursor)


api.add_resource(TodoList, '/todos')


 
if __name__ == '__main__':
     app.run(debug = True)
     
