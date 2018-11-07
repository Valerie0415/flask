#coding=utf-8
import json
import MySQLdb
from flask import abort,Flask,request,jsonify
# from flask import Flask
# from flask import request
# from flask import jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse



app = Flask(__name__)
api = Api(app)

#连接数据库
def connectdb():
	db=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='mydb',port=3306)
	cursor=db.cursor(cursorclass = MySQLdb.cursors.DictCursor)
	return (db,cursor)
    
#关闭数据库
def closedb():
	db.close()
	cursor.close()



class FormList(Resource):
    def get(self):
        try: 
            (db,cursor)=connectdb()
            cursor.execute('select * from devices')
            datas = cursor.fetchall()        
            return jsonify({"datas":datas})
            closedb(db,cursor)
        except Exception as e:
            self.send_error(500, '%s' % e);



api.add_resource(FormList, '/v1/device/:id')


 
if __name__ == '__main__':
    app.run(debug = True)
     
