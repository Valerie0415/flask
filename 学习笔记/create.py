import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", db="mydb")
cursor = db.cursor()

cursor.execute("create table xujie(name char(8), age int)")