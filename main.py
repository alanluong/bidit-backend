from config import db, app, manager
from models import *
from flask import jsonify

manager.create_api(Ad, methods=['GET', 'POST'])
manager.create_api(User, methods=['GET', 'POST'])
manager.create_api(Bid, methods=['GET', 'POST'])

@app.route('/login')
def login():
	return 'enter a login'

@app.route('/create_testdb')
def create_testdb():
	db.create_all()
	return 'created tables'

@app.route('/user')
def get_user():
	users = [user.serialize() for user in User.query.all()]
	return jsonify(users=users)

if __name__ == '__main__':
	app.run(debug=True)
