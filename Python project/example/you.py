from flask import Flask
from flask import request
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import config
 
databaseurl = 'mysql://root:123456@127.0.0.1:3306/mydb' 
# % (config.root, config.123456, config.localhost, config.3306, config.mydb)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = databaseurl
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


 @app.route('/', methods=['GET'])
 def list():
    (db.cursor)=connectdb()
    cursor.execute('select * from devices')
    

# class mytable(db.Model):
   
#     id = db.Column(db.Integer, primary_key=True, nullable=False)
#     name = db.Column(db.String(20), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
 
#     def __init__(self, id, name, age):
#         self.id = id
#         self.name = name
#         self.age = age
 
#     def __repr__(self):
#         return '' % (self.id, self.name)

# db.create_all()

# @app.command
# def query_all()
#     for u in users:
#         print u 
# @app.route('/', methods=['POST'])
# def hello():
#     if not request.json:
#         return "failed!", 400
#     student = {
#         'id': request.json['id'],
#         'name': request.json['name'],
#         'age': request.json['age']
#     }
    
#     stu = mytable(int(student['id']), student['name'], int(student['age']))
   
#     db.session.add(stu)
   
#     db.session.commit()
#     return "Hello World!"
 
# @app.route('/', methods=['GET'])
# def get_one():
#     if not request.args['id']:
#         abort(400)
#     get_id = request.args['id']

#     ids = mytable.query.all()

#     get = mytable.query.filter_by(id = get_id).first()

#     ret = 'id=%d,name=%s,age=%d' % (get.id, get.name, get.age)
#     return ret






# class apiHandler(BaseHTTPRequestHandler):
#     def dict_factory(self, cursor, row):
#         d = {}
#         for idx, col in enumerate(cursor.description):
#             d[col[0]] = row[idx]
#         return d

#     def datapoint(self, device_id):
#         parser_db = 'parser.db'
#         conn = sqlite3.connect(parser_db)
#         conn.row_factory = self.dict_factory
#         c = conn.cursor()
#         c.execute('SELECT datapoint, created FROM datapoints WHERE device_id = ?', (device_id,))
#         return (json.dumps(c.fetchall()))

#     def do_GET(self):
#         try:
#             mimeType = 'application/json'
#             self.send_response(200)
#             self.send_header('content-type', mimeType)
#             self.end_headers()
#             datapoints = self.datapoint('123456')
#             self.wfile.write(datapoints)
#             return
#         except Exception as e:
#             self.send_error(500, '%s' % e);





# if __name__ == '__main__':

#      app.run(debug = True)

