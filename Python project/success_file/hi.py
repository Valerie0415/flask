import json
import MySQLdb
import datetime
from flask import abort
from flask import Flask
from flask import request
from flask import jsonify

# import MySQLdb.cursors


app = Flask(__name__)
# app.config.from_object(__name__)



def connectdb():
	db=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='mydb',port=3306)
	cursor=db.cursor()
	return (db,cursor)


def closedb():
	db.close()
	cursor.close()


@app.route('/', methods=['GET'])
def main():
    (db,cursor)=connectdb()
    cursor.execute('select * from devices')
    #return (json.dumps(cursor.fetchall()))
    datas = cursor.fetchall()
    return jsonify({"datas":datas})
    # for data in datas:
    #     print data[:]
    
    closedb(db,cursor)


 
if __name__ == '__main__':
     app.run(debug = True)
     
