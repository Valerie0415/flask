import requests, json
import pymysql

sql="SELECT start_time,event_describe,REPLACE(event_analyse,'\n','') FROM jenkin_malfunction_faultls order by id DESC limit 1"
def connect_select(sql):
    conn = pymysql.connect(
        host="172.16.80.114",
        port=3306,
        user="novaops", 
        password="novaops", 
        database="novaops", 
        charset="utf8")
    cur = conn.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    return data
datas=connect_select(sql)
print(datas)
title=datas[0][0].strftime('%Y/%m/%d')+'-'+datas[0][1]
print(title)

# print(datas[0][1],datas[0][2])

pageData = {"version": {"number": 2},"type":"page","title":'nihao', "ancestors":[{"id":3214558}], "space":{"key":"novacloud"},"body":{"storage":{"value":datas[0][2],"representation":"storage"}}}
r = requests.put('http://wiki.vnnox.net/rest/api/content/3216245',
    data=json.dumps(pageData),
    auth=('xujie1', 'xujie578395620'),
    headers=({'Content-Type':'application/json'}))

print(r.text)