#-*- coding: UTF-8 -*- 
#实现简单的http服务
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import sep, curdir
import requests
import json


class GetHandler(BaseHTTPRequestHandler):
            
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        resp = requests.get('http://127.0.0.1:5000/v1/device/:id')
        html = '<h2>Show The Device Information</h2>'
        datapoints = json.loads(resp.text[12:-3]) #将字符串解析成json
        html += '<table><tr><th>Uuid</th><th>Token</th><th>Mac</th>'
        for d in datapoints:
            html += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % ( d['uuid'], d['token'], d['mac'])
        html += '<table>'
        self.wfile.write(html)
        return

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8082), GetHandler)
    print 'http://127.0.0.1:8082'
    server.serve_forever()

