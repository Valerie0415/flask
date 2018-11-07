#!/usr/bin/env python
#datas = {'ID'：0,'uuid'：1,'token':2,'mac':3,'latest_online_date':4,'latest_offline_date':5,'firmware_id':6,'hardware_id':7,'batch_id':8,'product_id':9,'installation':10,'installation_date':11,'longtitude':12,'latitude':13,'quality_inspector':14,'measurement_period':15,'public_key':16,'private_key':17,'created':18,'modified':19}


# html += '<table><tr><th>ID</th><th>uuid</th><th>token</th><th>mac</th><th>latest_online_date</th><th>latest_offline_date</th><th>firmware_id</th><th>hardware_id</th><th>batch_id</th><th>product_id</th><th>installation</th><th>installation_date</th><th>longtitude</th><th>latitude</th><th>quality_inspector</th><th>measurement_period</th><th>public_key</th><th>private_key</th><th>created</th><th>modified</th>'
        # for d in datas:
        #     html += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (d['ID'], d['uuid'], d['token'], d['mac'], d['latest_online_date'], d['latest_offline_date'], d['firmware_id'], d['hardware_id'], d['batch_id'], d['product_id'], d['installation'], d['installation_date'], d['longtitude'], d['latitude'], d['quality_inspector'], d['measurement_period'], d['public_key'], d['private_key'], d['created'], d['modified'])
        # html += '<table>'
        # self.wfile.write(html)
 



from flask import Flask
from flask.ext.restful import reqparse, Api, Resource, fields, marshal_with
from pymongo import MongoClient
from flask_restful import reqparse
from flask_restful import Resource, Api
																				
mongo_url = 'your-ip'
db_name = 'your-db'
col_name = 'your-col'
client = MongoClient(mongo_url)
col = client[db_name][col_name]
col.remove({})
col.insert({'_id': 1, "name": "debugo", "values": [70, 65]})
col.insert({'_id': 2, "name": "leo", "values": [65]})
app = Flask(__name__)
api = Api(app)
 
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('values', type=int, help='rate is a number', action='append')
 
 
class UserInfo(Resource):
    def get(self):
        return [str(i) for i in col.find({})]
 
    def post(self):
        args = parser.parse_args()
        user_id = col.count() + 1
        col.insert({'_id': user_id, "name": args["name"], "values": args["values"]})
        return [str(i) for i in col.find({'_id': user_id})], 201
 
api.add_resource(UserInfo, '/')
 
if __name__ == '__main__':
    app.run(debug=True)