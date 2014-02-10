from config import db, app
from models import *

@app.route("/login")
def login():
	return "enter a login"

@app.route('/create_testdb')
def create_testdb():
	test = Ad('test@testing.com', 50, 'testingggg' )
	db.session.add(test)
	db.session.commit()
	return 'created tables'

@app.route('/create_testdb_del')
def del_test():
	test = Ad.query.filter_by(uploader_email='test2@testing.com').first()
	print test.price
	db.session.delete(test)
	db.session.commit()
	return 'delete entry'



if __name__ == '__main__':
	app.run(debug=True)
