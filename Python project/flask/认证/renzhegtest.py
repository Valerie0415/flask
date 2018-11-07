import requests
# r = requests.get('http://127.0.0.1:5000/login',auth=('Valerie','12345'))  
# print r.text
token = 'VmFsZXJpZTowLjA0NjQ5ODkxNjkwNzk6MTUwMjQ1MzkyMC40NQ=='  
r = requests.get('http://127.0.0.1:5000/testlogin',params={'token':token})  
print r.text 