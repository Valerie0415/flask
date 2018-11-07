from flask_script import Manager
from app import app,db
from models import User

manager=Manager(app)

@manageer.command
def save():
    user=User(2,'xu',23)
    db.session.add(user)

    db.session.commit()
@manageer.command
def query_all():
    user=User.query_all()
    for u in users：
    print u
if __name__ == '__main__':

     manager.run()