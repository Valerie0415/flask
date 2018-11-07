#-*- coding: UTF-8 -*- 
from os import sep, curdir
import cgi
import requests
import logging
import json
from flask import abort
from flask import Flask,render_template
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/',methods=['GET'])           
def index(self):
    r = requests.get('http://127.0.0.1:5000/v1/device/:id')
    #return r.text[12:-3]
    datas=json.loads(r.text[12:-3])  #将字符串解析成json,即序列化       
    #return datas
   
    return render_template('index.html',datas=datas)


 
if __name__ == '__main__':
     app.run(debug = True,port=8001)
             
