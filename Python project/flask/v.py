#-*- coding: UTF-8 -*- 
import re
from os import sep, curdir
import cgi
import requests
import json
from flask import abort
from flask import Flask
from flask import request
from flask import jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse


app = Flask(__name__)
api = Api(app)

class Views(Resource):

    def get(self):
        r = requests.get('http://127.0.0.1:5000/v1/device/product/111111')
        #return r.text
        html = '<h2>Device Information</h2>'
        datas=json.loads(r.text[12:-3])  #将字符串解析成json       
        #return datas
        html += '<table><tr><th>Batch_id</th><th>ID</th><th>Product_id</th>'
        for d in datas:
            html += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % ( d['uuid'], d['token'], d['mac'])
        html += '<table>'
        #self.html.append(html) 
        response(html)     
        return 
       
api.add_resource(Views, '/views')


 
if __name__ == '__main__':
     app.run(debug = True,port=8080)
             
