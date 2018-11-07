
from os import sep, curdir
import cgi
import requests
import logging
import json
from flask import abort
from flask import Flask
from flask import request
from flask import jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse


app = Flask(__name__)
api = Api(app)


class views(Resource):            
    def get(self):   	
        # r = requests.get('http://127.0.0.1:5000/forms')
        r = requests.get('http://127.0.0.1:5000/v1/device/:id')
        
        # return r.text
        datas=json.loads(r.text)
        #return (json.lodas(r.text))
        return datas
       
api.add_resource(views, '/views')


 
if __name__ == '__main__':
     app.run(debug = True,port=8080)
             
