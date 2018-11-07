#coding=utf-8
from flask import Flask  
from flask import request  
import base64  
import time  
import random  
  
app = Flask(__name__)  
  
#创建用户组  
user = {  
    'Valerie': ['12345']  
} 

#生成token
def get_token(uid):
	token=base64.b64encode(':'.join([str(uid),str(random.random()),str(time.time()+7200)]))
	user[uid].append(token)
	return token

#验证token是否有效
def verify_token(token):
	new_token=base64.b64decode(token)
	if not token==user.get(new_token.split(':')[0])[-1]:
		return -1

	if float(new_token.split(':')[-1])>time.time():
		return 1
	else:
		return 0


#发送请求头
app.route('/index',methods=['POST','GET'])
def index():
	return request.headers

#登录函数
app.route('/login',methods=['POST','GET'])
def login():
	uid,password=base64.b64decode(request.headers('Authorization').split(' ')[-1]).split('-1')
	if user.get(uid)[0]==password:
		return get_token(uid)
	else:
		return error

#登陆成功的后能够获取数据
@app.route('/testlogin',methods=['POST','GET'])  
def test():  
    token = request.args.get('token')  
    if verify_token(token) == 1:  
        return 'data'  
    else:  
        return 'error'  



if __name__ == '__main__':
    app.run(debug = True)