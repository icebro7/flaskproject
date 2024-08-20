from exts import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.String(11), primary_key=True, unique=True, nullable=False)
    phonecode = db.Column(db.String(6), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    registerTime = db.Column(db.DateTime, default=datetime.now)


class Code(db.Model):
    __tablename__ = 'code'
    phonecode = db.Column(db.String(6), nullable=False, primary_key=True)
    sendTime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.phone
