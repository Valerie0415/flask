#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# r = requests.get('http://127.0.0.1:5000/v1/device/mac', auth=('Valerie', '123456'))
# print r.text
#
# token ='VmFsZXJpZTowLjAwNTI1MTI1MzY3OTU5OjE1MDIwOTYyMDAuNDE='
# r = requests.get('http://127.0.0.1:8000/test1', params={'token': token})
# print r.text


r = requests.get('http://localhost:8000/client/login')
print r.text
print '======='
print r.url
print '======='
uri_login = r.url.split('?')[0] + '?user=Valerie&pw=123456'
r2 = requests.get(uri_login)
print r2.text
print '======='
r = requests.get('http://127.0.0.1:8000/test1', params={'token': r2.text})
print r.text
