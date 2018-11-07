
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
        r = requests.get('http://127.0.0.1:5000/forms')
        # data=r.text
        # return data
        datas = json.loads(r.text)['datas'][2]
      
        
        html = '<table><tr><th>ID</th><th>batch_id</th><th>created</th><th>firmware_id</th><th>hardware_id</th><th>installation</th><th>installation_date</th><th>latest_offline_date</th><th>latest_online_date</th><th>latitude</th><th>longtitude</th><th>mac</th><th>measurement_period</th><th>modified</th><th>private_key</th><th>product_id</th><th>public_key</th><th>quality_inspector</th><th>token</th><th>uuid</th>'
        html = '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (['ID'], ['batch_id'], ['created'], ['firmware_id'], ['hardware_id'], ['installation'], ['installation_date'], ['latest_offline_date'], ['latest_online_date'], ['latitude'], ['longtitude'], ['mac'], ['measurement_period'], ['modified'], ['private_key'], ['product_id'], ['public_key'], ['quality_inspecto'], ['token'], ['uuid'])
        html = '<table>'
        r.write (html)
        r.close() 
        return 
       
api.add_resource(views, '/views')


 
if __name__ == '__main__':
     app.run(debug = True,port=8000)
             
