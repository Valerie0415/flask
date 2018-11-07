from flask import Flask
from flask import request
from flask import jsonify
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import config
databaseurl = 'mysql://root:123456@127.0.0.1:3306/mydb' 
# % (config.root, config.123456, config.localhost, config.3306, config.mydb)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = databaseurl
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

from sqlalchemy import Column, Integer, String, Sequence

class mytable(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
  
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
   
    def __repr__(self):
        # return '' % (self.id, self.name)
        return "<User(name='%s', age='%s', id='%s')" % (self.name, self.age, self.id)

db.create_all()
 
@app.route("/")
def main():
    db = mytable(config)
    result = db.session.query(User).filter_by(name="xu").first()
    return jsonify({"result":result})     

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
#     #stu = mytable(2,'xu',24)
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

if __name__ == '__main__':
    app.run(debug = True)

     