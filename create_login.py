from flask import Flask, flash
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
import random
import time
from sqlalchemy import event
from sqlalchemy import DDL
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='admin', passwd='aaggss',db='login')
cur = conn.cursor()

app = Flask (__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:aaggss@localhost/login'

class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64))
    username = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    def __init__(self,arg):
        self.id = arg['id']
        self.email = arg['email']
        self.username = arg['username']
        self.password_hash = arg['password_hash']



    def __repr__(self):
        return '<username: %r Password: %r>' % (self.username,self.password_hash)

class database_users():
    def db_init(self):
        db.create_all()
    def drop_all(self):
        db.drop_all()
    def insertDb(self):
        try:
            arg={}
            arg['id']           = 1
            arg['email']        = 'admin@mail.com'
            arg['username']     = 'admin'
            arg['password_hash'] = generate_password_hash('admin')
            
            data=users(arg)
            print data
            db.session.add(data)
            db.session.commit()
        except Exception as e:
            #flash('insertDb: '+str(e))
            print 'insertDb: '+str(e)
def table_create():
    cur.execute('CREATE TABLE users (id INTEGER NOT NULL AUTO_INCREMENT,\
     email VARCHAR(64),\
     username VARCHAR(64),\
     password_hash VARCHAR(128),\
     PRIMARY KEY (id))')

table_create()
users_obj = database_users()
users_obj.insertDb()