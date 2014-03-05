from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager
from flask.ext.login import LoginManager

PORT = 5000
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bidit:bidit@ec2-54-213-102-70.us-west-2.compute.amazonaws.com/bidit'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bidit:bidit@ec2-54-213-102-70.us-west-2.compute.amazonaws.com/bidit_test'
db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db = db)
login = LoginManager(app)
