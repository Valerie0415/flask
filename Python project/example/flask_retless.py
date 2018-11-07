import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
 
 
app = Flask(__name__)
db = SQLAlchemy(app)
restless = APIManager(app, flask_sqlalchemy_db=db)
 
 
class User(db.Model):
	# __tablename__ = 'user'
    """
    user
    """
 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    login_time = db.Column(db.DateTime)
 
 
restless.create_api(User, methods=['GET', 'POST', 'DELETE', 'PATCH', 'PUT'], results_per_page=100)
 
db.create_all()
 
if __name__ == '__main__':
    app.run(port=25000)