from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

Db = SQLAlchemy()


class User(Db.Model):
    __tablename__ = 'users'
    uid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    username = Db.Column(Db.String(64), unique=True, nullable=False)
    password = Db.Column(Db.String(128), nullable=False)


class Condo(Db.Model):
    __tablename__ = 'posts'
    cid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    mlsnum = Db.Column(Db.Integer, primary_key=True)
    zip = Db.Column(Db.Integer, primary_key=True)
    bed = Db.Column(Db.Integer, primary_key=True)
    bath = Db.Column(Db.Integer, primary_key=True)
    sqft = Db.Column(Db.Integer, primary_key=True )
    listprice = Db.Column(Db.Integer, primary_key=True)
    photourl = Db.Column(Db.String(1024), nullable=False)


class Photos(Db.Model):
    __tablename__ = 'photos'
    pid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    mlsnum = Db.Column(Db.Integer, Db.ForeignKey('users.uid'), nullable=False)
    imgnum = Db.relation(User, backref="photos")
