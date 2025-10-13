from db import db
from flask_login import UserMixin
 
class User(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

class Task(db.Model, UserMixin):
    __tablename__ = "Tasks"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    task = db.Column(db.String)
