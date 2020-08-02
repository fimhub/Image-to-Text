from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import HSTORE

Db = SQLAlchemy()

class User(Db.Model):
    __tablename__ = 'users'
    uid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    username = Db.Column(Db.String(64), unique=True, nullable=False)
    password = Db.Column(Db.String(128), nullable=False)


class Condo(Db.Model):
    __tablename__ = "condos"
    uid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    mls_num = Db.Column(Db.Integer, nullable=False)
    beds = Db.Column(Db.Integer, nullable=False)
    baths = Db.Column(Db.Integer, nullable=False)
    sqft = Db.Column(Db.Integer, nullable=False)
    age = Db.Column(Db.Integer, nullable=False)
    lot_size = Db.Column(Db.Integer, nullable=False)
    garage = Db.Column(Db.Integer, nullable=False)
    list_price = Db.Column(Db.Integer, nullable=False)
    sold_price = Db.Column(Db.Integer, nullable=False)
    city = Db.Column(Db.String(64), nullable=False)
    state = Db.Column(Db.String(64), nullable=False)
    zip = Db.Column(Db.String(64), nullable=False)
    photo_url = Db.Column(Db.String(64), nullable=False)


class Photo(Db.Model):
    __tablename__ = 'photos'
    pid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    mlsnum = Db.Column(Db.Integer, nullable=False)
    imgnum = Db.Column(Db.Integer, nullable=False)
    features = Db.Column(HSTORE, nullable=False)
