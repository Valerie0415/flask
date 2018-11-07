#coding=utf-8
from flask import Flask,request

app=Flask(__name__)

#新建一个客户端，并保存到用户字典
user = {  
    'Valerie': ['12345']  
} 
client_id = '1234567890'  
user[client_id] = []  
auth_code = {}  
oauth_redirect_uri = []
redirect_uri='http://localhost:5000/client/passport'

#授权服务器实现生成授权码功能
def gen_auth_code(uri):  
    code = random.randint(1,1000)  
    auth_code[code] = uri  
    return code 

@app.route('/index',methods=['POST','GET'])
def index():
	print request.headers
	return 'hello world!'


#cleint端重定向到认证服务器
@app.route('/client/login',methods=['POET','GET'])
def client_login():
	uri='http://127.0.0.1:5000/oauth?response_type=code&client_id=%s&redirect_uri=%s' %(client_id,redirect_uri)
	return redirect(uri)

@app.route('/oauth',methods=['POST','GET'])
def oauth():
	if request.args.get('redirect_uri'):  #授权服务器需要实现保存redirect_uri功能
        oauth_redirect_uri.append(request.args.get('redirect_uri'))
	if request.args.get('user'):          #授权服务器需要实现发放授权码功能
		if user.get(request.args.get('user'))[0] == request.args.get('pw') and oauth_redirect_uri: 
			uri = oauth_redirect_uri[0] + '?code=%s' % gen_auth_code(oauth_redirect_uri[0]) 
	        return redirect(uri) 
    if request.args.get('code'):  
        if auth_code.get(int(request.args.get('code'))) == request.args.get('redirect_uri'):  
            return gen_token(request.args.get('client_id'))


#client实现请求token的功能
@app.route('/client/passport', methods=['POST', 'GET'])  
def client_passport():  
    code = request.args.get('code')  
    uri = 'http://localhost:5000/oauth?grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s' % (code, redirect_uri, client_id)  
    return redirect(uri)



if __name__ == '__main__':
    app.run(debug = True)