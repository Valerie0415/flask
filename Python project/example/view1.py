
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
        html = '<h2>Devices Information</h2>'
        datas=r.text      
        data = json.loads(datas)
        html += '<table><tr><th>ID</th><th>batch_id</th><th>created</th><th>firmware_id</th><th>hardware_id</th><th>installation</th><th>installation_date</th><th>latest_offline_date</th><th>latest_online_date</th><th>latitude</th><th>longtitude</th><th>mac</th><th>measurement_period</th><th>modified</th><th>private_key</th><th>product_id</th><th>public_key</th><th>quality_inspector</th><th>token</th><th>uuid</th>'
        for d in data:
        	html += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (d['ID'], d['batch_id'], d['created'], d['firmware_id'], d['hardware_id'], d['installation'], d['installation_date'], d['latest_offline_date'], d['latest_online_date'], d['latitude'], d['longtitude'], d['mac'], d['measurement_period'], d['modified'], d['private_key'], d['product_id'], d['public_key'], d['quality_inspecto'], d['token'], d['uuid'])
        html += '<table>'
        self.wfile.write(html)
        return 
       
api.add_resource(views, '/views')


 
if __name__ == '__main__':
     app.run(debug = True,port=8080)
             
