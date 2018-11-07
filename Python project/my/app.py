from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/mydb'
db = SQLAlchemy(app)
 @app.route('/')
 def hello_world():
     return 'hello world!'
if __name__ == '__main__':

     app.run()