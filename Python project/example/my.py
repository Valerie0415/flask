from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import jsonify
app = Flask(__name__)
Base = declarative_base()
class Database(object):    
    def __init__(self, configure):        
        self.configure = configure        
        self.engine = create_engine(self.configure.MYSQL_SQLALCHEMY_URL)        
        self.Session = sessionmaker(bind=self.engine)        
        self.session = self.Session()
 
from sqlalchemy import Column, Integer, String, Sequence
class User(Base):
    """
       user table
    """
    __tablename__ = 'users'
    id = Column(Integer, Sequence("USER_ID_SEQ"), primary_key=True)
    username = Column(String(256), doc=u"user")
    password = Column(String(256), doc=u"passwd")
 
    def __repr__(self):
        return "<User(username='%s', password='%s', id='%s')" % (self.username, self.password, self.id)

@app.route("/")
def main():
    db = Database(config)
    result = db.session.query(User).filter_by(username="aa").first()
    return jsonify({"result":result})        

if __name__ == '__main__':

     app.run(debug = True)