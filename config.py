from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager
from flask.ext.login import LoginManager

PORT = 5000
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bidit:bidit@ec2-54-213-102-70.us-west-2.compute.amazonaws.com/bidit'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bidit:bidit@ec2-54-213-102-70.us-west-2.compute.amazonaws.com/bidit_test'
app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
db = SQLAlchemy(app)
api_manager = APIManager(app, flask_sqlalchemy_db = db)
login_manager = LoginManager(app)
