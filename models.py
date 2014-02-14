from config import db



class User(db.Model):
	__tablename__ = 'User'
	email = db.Column(db.String(50), primary_key=True)
	first_name = db.Column(db.String(45))
	last_name = db.Column(db.String(45))

	def __init__(self, email, fn, ln):
		self.email = email
		self.first_name = fn
		self.last_name = ln
	
	def serialize(self):
		return {
			'email': self.email,
			'first_name': self.first_name,
			'last_name': self.last_name
		}

class Ad(db.Model):
	__tablename__ = 'Ad'
	uploader_email = db.Column(db.String(50), primary_key=True)
	price = db.Column(db.Integer)
	description = db.Column(db.String(45))

	def __init__(self, uploader_email, price, description):
		self.uploader_email = uploader_email
		self.price = price
		self.description = description
