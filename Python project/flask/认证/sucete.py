import requests 

r = requests.get('http://127.0.0.1:5000/login',auth=('Valerie','12345'))  
print r.text 

# token = 'VmFsZXJpZTowLjIwODM1MzQ4ODc4ODoxNTAyNDUyMjUwLjc2'  
# r = requests.get('http://127.0.0.1:8000/testlogin',params={'token':token})  
# print r.text 
