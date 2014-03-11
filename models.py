from config import db
from flask.ext.login import UserMixin

class Ad(db.Model):
	__tablename__ = 'Ad'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(50), db.ForeignKey("User.email"), nullable=False)
	price = db.Column(db.Numeric(15,2))
	description = db.Column(db.String(45))
	image_path = db.Column(db.String(45))

	def __init__(self, email, price, description, image_path=None):
		self.email = email
		self.price = price
		self.description = description
		self.image_path = image_path 

class Bid(db.Model):
	__tablename__ = 'Bid'
	id = db.Column(db.Integer, primary_key=True)
	price = db.Column(db.Numeric(15,2), nullable=False)
	bidder = db.Column(db.String(50), db.ForeignKey("User.email"), nullable=False)
	seller = db.Column(db.String(50), db.ForeignKey("User.email"), nullable=False)
	ad_id = db.Column(db.Integer, db.ForeignKey("Ad.id"), nullable=False)

	def __init__(self, price, bidder, seller, ad_id):
		self.price = price
		self.bidder = bidder
		self.seller = seller
		self.ad_id = ad_id

class Message(db.Model):
	__tablename__ = 'Message'
	id = db.Column(db.Integer, primary_key=True)
	sender = db.Column(db.String(50), db.ForeignKey("User.email"), nullable=False)
	receiver = db.Column(db.String(50), db.ForeignKey("User.email"), nullable=False)
	content = db.Column(db.Text)

	def __init__(self, sender, receiver, content):
		self.sender = sender 
		self.receiver = receiver 
		self.content = content

class User(db.Model, UserMixin):
	__tablename__ = 'User'
	email = db.Column(db.String(50), primary_key=True)
	password = db.Column(db.String(50))
	first_name = db.Column(db.String(45))
	last_name = db.Column(db.String(45))

	def __init__(self, email, password, first_name, last_name):
		self.email = email
		self.password = password
		self.first_name = first_name
		self.last_name = last_name
	
	def get_id(self):
		return self.email
	
	def serialize(self):
		return {
			'email': self.email,
			'password': self.password,
			'first_name': self.first_name,
			'last_name': self.last_name
		}
