from config import db, app

@app.route("/login")
def login():
	return "enter a login"

@app.route('/create_testdb')
def create_testdb():
	db.create_all()
	test = Ad('test@testing.com', 23, 'this is a test ad')
	db.session.add(test)
	db.session.commit()
	return 'created tables'

if __name__ == '__main__':
	app.run(debug=True)
