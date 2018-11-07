import requests
##r = requests.get('http://127.0.0.1:5000/login',auth=('Valerie','12345'))  
##print r.text 

token = 'VmFsZXJpZTowLjE4NDMzNDY3NjgyMzoxNTA0NTI1MjcxLjU3'  
r = requests.get('http://127.0.0.1:5000/device/mac',params={'token':token})  
print r.text
