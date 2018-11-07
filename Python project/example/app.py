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
            resp = requests.get('http://127.0.0.1:5000/forms')
            html = '<h2>Device: 123456</h2>'
            # html = '<h2>Devices Information</h2>'
            datapoints = json.loads(resp.text)
            html += '<table><tr><th>ID</th><th>uuid</th><th>token</th><th>mac</th><th>latest_online_date</th><th>latest_offline_date</th><th>firmware_id</th><th>hardware_id</th><th>batch_id</th><th>product_id</th><th>installation</th><th>installation_date</th><th>longtitude</th><th>latitude</th><th>quality_inspector</th><th>measurement_period</th><th>public_key</th><th>private_key</th><th>created</th><th>modified</th>'
            for d in datapoints:
                html += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (d['ID'], d['uuid'], d['token'], d['mac'], d['latest_online_date'], d['latest_offline_date'], d['firmware_id'], d['hardware_id'], d['batch_id'], d['product_id'], d['installation'], d['installation_date'], d['longtitude'], d['latitude'], d['quality_inspector'], d['measurement_period'], d['public_key'], d['private_key'], d['created'], d['modified'])
            html += '<table>'
            self.wfile.write(html)
                # fp.close()
            return
        except Exception as e:
            self.send_error(500, '%s' % e);

def run_app_server():
    PORT = 8000
    try:
        ser = HTTPServer(('', PORT), appHandler) 
        print 'Start API Server' ,
        ser.serve_forever()
    except KeyboardInterrupt:
        print 'Shutting down the server.'
        ser.socket.close()  

run_app_server()
