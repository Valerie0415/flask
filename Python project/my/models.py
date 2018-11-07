import MySQLdb
from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
