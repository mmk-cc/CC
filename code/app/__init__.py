from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy, orm 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#Create an Instance of Flask
app = Flask(__name__)

#Include config from config.py
app.config.from_object('config')
app.secret_key = 'nosecret'


#Create an instance of SQLAclhemy
db = SQLAlchemy(app)


from app import views, models


