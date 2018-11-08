# -*-coding:utf8-*-
from flask import Flask
from flask import jsonify
from flask import request 
import datetime
import redis
import json
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

conninfo ={
	"cn":'r-bp1a0b8117d51654.redis.rds.aliyuncs.com',
	"jp":'172.24.1.233',
	"eu":'r-gw81ce9ba8349594.redis.germany.rds.aliyuncs.com',
	"us":'r-rj912bac22e73a84.redis.rds.aliyuncs.com',
	"au":'r-p0w06c79ff8d3aa4.redis.australia.rds.aliyuncs.com',
	"in":'r-a2d5327b5cbc2134.redis.ap-south-1.rds.aliyuncs.com',
}

def select_area(m):
	x=conninfo.keys()
	for i in x:
		print(conninfo[i])
		if m=="jp" and m==i:
			hosts=conninfo[i]
			psd="1f494c4e0df9b837dbcc82eebed35ca3f2ed3fc5f6428d75bb542583fda2170f"
			prots=19000
		elif m!="jp" and m==i:
			hosts=conninfo[i]
			psd='vLHg5t9UemBzQbaC1CNQ'
			ports=6379
	return hosts,ports,psd


class select(Resource):

	def get(self,area,date_time):
		area=area.encode("utf-8")
		x=select_area(area)
		playlists = []
		time_date = (datetime.datetime.now()-datetime.timedelta(days=date_time)).strftime('%Y-%m-%d %H:%M:%S')
		pool = redis.ConnectionPool(host=x[0],port=x[1],password=x[2])
		r=redis.Redis(connection_pool=pool)

		keylist = r.keys("MONITOR_LAST_HEARTBEAT*")

		for key in keylist:
			keyvalue=r.get(key)
			todict=json.loads(keyvalue)
			heartTime=todict.get('time')
			if heartTime is None:
				continue
			if heartTime>time_date:
				playlists.append(int(key.split("_")[-1].replace("HEARTBEAT","")))
		length=len(playlists)
		data={"项目":Vnnox,"发布节点":area,"活跃终端数":length,"时间段":date_time}
		return jsonify({"result":data})
		# return jsonify({"result":data}),{'Access-Control-Allow-Origin':'*'}


api.add_resource(select, '/vnnox/<string:area>/<int:date_time>')

if __name__ == '__main__':
	app.config['JSON_AS_ASCII'] = False
	app.run(debug=True)