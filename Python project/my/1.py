import  MySQLdb as mdb
con = mdb.connect(
	host = 'localhost',
	port = 3306,
	user = 'root',
	passwd = '123456',
	db = 'ceshi',
	charset='utf8')
cur = con.cursor()