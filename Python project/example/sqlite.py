#coding=utf-8
 
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
 
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E:/app.db'
db = SQLAlchemy(app)
 
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(30))
     
    def __init__(self, id, user_name):
        self.id = id
        self.user_name = user_name
         
    def __repr__(self):
        return '<User %r>' % self.user_name
 
 
@app.route('/')
def index():
    return 'flask'
 
 
if __name__ == '__main__':
    db.create_all()
    app.run(port = 80)