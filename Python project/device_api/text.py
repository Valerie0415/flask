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
# api = restful_extend.ErrorHandledApi(app)


def connectdb():
	db=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='mydb',port=3306)
	cursor=db.cursor(cursorclass = MySQLdb.cursors.DictCursor)
	return (db,cursor)
      

def closedb():
	db.close()
	cursor.close()

# class MyRoutes(Resource):
#     def get(self):
#         raise Exception("errmsg:404")




# def error_404():    
#         respons = dict(status=0, message="404 Not Found")
#         return jsonify(respons)
class Form(Resource):
    
    



    # def error_200(error):        
    #     response = dict(status=0, message="200 Ok")
    #     return jsonify(response), 200

    def get(self,data_id):
        # (respons)=error_404()
        # (response)=error_200()
        (db,cursor)=connectdb()
        #cursor.execute('select id,mac,product_id from devices')
        cursor.execute('select * from devices')
        datas = cursor.fetchall()        
        #data = filter(lambda t: t['id'] == data_id, datas)
        def abort_if_todo_doesnt_exist(data_id):
                
            if data_id not in datas:
                abort(404, message='')
            parser = reqparse.RequestParser()
            parser.add_argument('id',type=int) 
        abort_if_todo_doesnt_exist(data_id)                 
        # if len(data) == 0:           
        #     abort(404)
        #     return jsonify(respons)
        #     return make_response(jsonify({'code':'404','message':'Not found'}),404)
        # return make_response(jsonify({'code':'200','message':'OK','data': data}),200)
        #return jsonify({'data': data},200)
        return datas[data_id]
        closedb(db,cursor)
 


api.add_resource(Form,'/v1/device/<int:data_id>')

 
if __name__ == '__main__':
    app.run(debug = True)
     
