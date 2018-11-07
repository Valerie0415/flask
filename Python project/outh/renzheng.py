#-*- coding: UTF-8 -*- 
import base64  
import time  
import random
import json
from flask import abort,Flask,request,jsonify
from flask.ext import restful
from influxdb import InfluxDBClient
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)  
api = restful.Api(app)  

user = {  
    'Valerie': ['12345']  
}  
  
  
 
def gen_token(uid):  
    token = base64.b64encode(':'.join([str(uid),str(random.random()),str(time.time() + 7200)]))  
    user[uid].append(token)  
    return token  
  
 
def verify_token(token):  
    _token = base64.b64decode(token)  
    if not user.get(_token.split(':')[0])[-1] == token:  
        return -1  
    if float(_token.split(':')[-1]) >= time.time():  
        return 1  
    else:  
        return 0  

client = InfluxDBClient('192.168.0.2', 8086, 'root', '', database='example') 
 
#到认证服务器获取token
class Mac(Resource):   
    def get(self):  
        uid,password = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).split(':')  
        if user.get(uid)[0] == password:  
            return gen_token(uid)  
        else:  
            return 'error'  
  
#判断token是否合法和有效，若有效则进入api
class Test(Resource):   
    def get(self):  
        token = request.args.get('token')  
        if verify_token(token) == 1:
            result = client.query('select * from product_4 limit 3')
		    # result = client.query('select * from mydb') 
            data_points=list(result.get_points())
            return data_points 
      
        else:  
            return 'please first verify token' 

api.add_resource(Mac, '/login')
api.add_resource(Test, '/device/mac') 
  
if __name__ == '__main__':  
    app.run(debug=True)  

