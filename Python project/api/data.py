#! /usr/bin/env python
#-*- coding:utf-8 -*-
import json
from flask.ext import restful
from flask import Flask, request, jsonify,abort
from influxdb import InfluxDBClient
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = restful.Api(app)

#client = InfluxDBClient('192.168.0.130', 8086, 'root', '', database='test') 
client = InfluxDBClient('192.168.0.2', 8086, 'root', '', database='example') 

class Data_All(Resource):
	def get(self):
		result = client.query('select * from product_4 limit 3')
		# result = client.query('select * from mydb') 
		data_points=list(result.get_points())
		return data_points 
		
class Data_One(Resource):
	def get(self):
		result = client.query('select current_A,energy_A,factor_A,frequency_A,power_A,voltage_A from product_4 limit 3')
		data_points=list(result.get_points())
		return data_points 		

class Data_Select(Resource):
	def get(self,data_id):
		result = client.query('select * from product_4 limit 3')
		data_points=list(result.get_points())
		# return data_points
		data = filter(lambda t: t['voltage_A'] == data_id, data_points)
		if len(data) == 0:
			abort(404)
		return jsonify({'data': data})
		

class Date_All(Resource):
	def get(self,data_id):
		#result = client.query('select * from product_4 where time>now() - 1d')
		result = client.query('select * from product_4 limit 3')
		# result = client.query('select * from mydb') 
		data_points=list(result.get_points())
		b=[]
		r=data_id.split(",")
		for i in r:   
			data = filter(lambda t: t['device'] == i, data_points)
			if len(data) == 0:
				abort(404)
			b.append(data)
		return jsonify(b)
		#return data_points 		 		

api.add_resource(Data_All, '/v1/datas/api')
api.add_resource(Data_One, '/v1/datas/api/data')
api.add_resource(Data_Select, '/v1/datas/api/<float:data_id>')
api.add_resource(Date_All, '/v1/datas/api/<string:data_id>')

if __name__ == '__main__':
	app.run(debug=True,port=8000)
