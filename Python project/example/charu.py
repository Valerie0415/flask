from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager,Shell
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/mydb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
manager = Manager(app)
db = SQLAlchemy(app)

class User(db.Model):
	 __tablename__ = 'hello'
	 id = db.Column(db.Integer, primary_key=True)
	 username = db.Column(db.String(64), unique=True)


	 def __repr__(self):
	 return '<User %r>' % self.username

	def make_shell_context():
	 return dict(app=app,db=db,User=User)
	manager.add_command('shell',Shell(make_context=make_shell_context))

if __name__ == '__main__':
manager.run()