import json
import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class LoanModel(db.Model):
    __tablename__ = 'loan'
    __table_args__ = {'schema':'LoanManagement'}

    id = db.Column(db.String(100), primary_key=True)
    loanName = db.Column(db.String(100),nullable=False)
    user_id = db.Column(db.String(100),nullable=False)
    userName = db.Column(db.String(100),nullable=False)

class UserModel(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'schema':'LoanManagement'}

    id = db.Column(db.String(100), primary_key=True)
    userName = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(1000000),nullable=False)