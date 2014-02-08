from config import db

class Ad(db.Model):
	uploader_email = db.Column(db.String(50), primary_key=True)
	price = db.Column(db.Integer)
	description = db.Column(db.String(45))

	def __init__(self, uploader_email, price, description):
		self.uploader_email = uploader_email
		self.price = price
		self.description = description
