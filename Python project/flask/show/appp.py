from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import sep, curdir
import cgi
import requests
import logging
import json

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

class appHandler(BaseHTTPRequestHandler):
            
    def do_GET(self):
        try:
            mimeType = 'text/html'
            
            self.send_response(200)
            self.send_header('content-type', mimeType)
            self.end_headers()
            resp = requests.get('http://127.0.0.1:5000/v1/device/:id')
            html = '<h2>Device Information</h2>'
            datapoints = json.loads(resp.text[12:-3]) #将字符串解析成json
            html += '<table><tr><th>batch_id</th><th>created</th><th>firmware_id</th><th>hardware_id</th><th>id</th><th>installation</th><th>installation_date</th><th>latest_offline_date</th><th>latest_online_date</th><th>latitude</th><th>longtitude</th><th>Mac</th><th>measurement_period</th><th>modified</th><th>private_key</th><th>product_id</th><th>quality_inspector</th><th>Mac</th><th>token</th><th>uuid</th>'
            for d in datapoints:
                html += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % ( d['batch_id'], d['created'], d['firmware_id'], d['hardware_id'], d['id'], d['installation'], d['installation_date'], d['latest_offline_date'], d['latest_online_date'], d['latitude'], d['longtitude'],d['mac'], d['measurement_period'],  d['modified'], d['private_key'], d['product_id'], d['public_key'], d['quality_inspector'], d['token'], d['uuid'])
            html += '<table>'
            self.wfile.write(html)
                # fp.close()
            return
        except Exception as e:
            self.send_error(500, '%s' % e);

def run_app_server():
    PORT = 8082
    try:
        ser = HTTPServer(('', PORT), appHandler) 
        print 'Start API Server' ,
        ser.serve_forever()
    except KeyboardInterrupt:
        print 'Shutting down the server.'
        ser.socket.close()  

run_app_server()
