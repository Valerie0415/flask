#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import random
import time

from flask import Flask, request, redirect

app = Flask(__name__)

users = {
    "Valerie": ["123456"]
}

redirect_uri='http://localhost:8000/client/passport'
client_id = '123456'
users[client_id] = []
auth_code = {}

oauth_redirect_uri = []

def gen_token(uid):
    token = base64.b64encode(':'.join([str(uid), str(random.random()), str(time.time() + 7200)]))
    users[uid].append(token)
    return token

def gen_auth_code(uri):
    code = random.randint(0,10000)
    auth_code[code] = uri
    return code

#验证token是否有效
def verify_token(token):
    _token = base64.b64decode(token)
    if not users.get(_token.split(':')[0])[-1] == token:
        return -1
    if float(_token.split(':')[-1]) >= time.time():
        return 1
    else:
        return 0

@app.route('/index', methods=['POST', 'GET'])
def index():
    print request.headers 
    return 'hello'

@app.route('/login', methods=['POST', 'GET'])
def login():
    uid, pw = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).split(':')
    if users.get(uid)[0] == pw:
        return gen_token(uid)
    else:
        return 'error'

@app.route('/oauth', methods=['POST', 'GET'])
def oauth():
    if request.args.get('user'):
        if users.get(request.args.get('user'))[0] == request.args.get('pw') and oauth_redirect_uri:
            uri = oauth_redirect_uri[0] + '?code=%s' % gen_auth_code(oauth_redirect_uri[0])
            return redirect(uri)
    if request.args.get('code'):
        if auth_code.get(int(request.args.get('code'))) == request.args.get('redirect_uri'):
            return gen_token(request.args.get('client_id'))
    if request.args.get('redirect_uri'):
        oauth_redirect_uri.append(request.args.get('redirect_uri'))
    return 'please login'

#用户登录客户端后重定向到认证服务器
@app.route('/client/login', methods=['POST', 'GET'])
def client_login():
    uri = 'http://localhost:8000/oauth?response_type=code&client_id=%s&redirect_uri=%s' % (client_id, redirect_uri)
    return redirect(uri)  #携带client ID+client URI

#认证服务器获得用户名、密码后重定向到client
@app.route('/client/passport', methods=['POST', 'GET'])
def client_passport():
    code = request.args.get('code')
    uri = 'http://localhost:8000/oauth?grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s' % (code, redirect_uri, client_id)
    return redirect(uri)   #携带client ID+client URI+code

@app.route('/test1', methods=['POST', 'GET'])
def test():
    token = request.args.get('token')
    if verify_token(token) == 1:
        url='http://127.0.0.1:5000/v1/device/mac'
        return redirect(url)
    else:
        return 'error'

if __name__ == '__main__':
    app.run(debug=True,port=8000)
