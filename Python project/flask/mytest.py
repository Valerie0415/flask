import requests  
  
r = requests.get('http://127.0.0.1:5000/login',auth=('Valerie','12345'))  
print r.text
print r.history 