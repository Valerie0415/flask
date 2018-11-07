from flask import Flask  
from flask import request  
import base64  
import time  
import random  
  
app = Flask(__name__)  
  
# user info  
user = {  
    'Valerie': ['12345']  
}  
  
  
# generate token  
def gen_token(uid):  
    token = base64.b64encode(':'.join([str(uid),str(random.random()),str(time.time() + 7200)]))  
    user[uid].append(token)  
    return token  
  
#verify token  
def verify_token(token):  
    _token = base64.b64decode(token)  
    if not user.get(_token.split(':')[0])[-1] == token:  #传进来的token与用户登陆时生成的token不一致，返回-1
        return -1  
    if float(_token.split(':')[-1]) >= time.time():  #一致并且token没有过期则返回1
        return 1  
    else:  
        return 0  
  
#if login success,return a token to user  
@app.route('/login', methods=['POST','GET'])  
def login():  
    uid,password = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).split(':')  
    if user.get(uid)[0] == password:  
        return gen_token(uid)  
    else:  
        return 'error'  
  
#create a test route for verify login success or not  
@app.route('/testlogin',methods=['POST','GET'])  
def test():  
    token = request.args.get('token')  
    if verify_token(token) == 1:  
        return 'login_success'  
    else:  
        return 'login_error'  

 
  
if __name__ == '__main__':  
    app.run(debug=True) 