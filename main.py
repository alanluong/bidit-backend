from config import db, app, manager, PORT, login
from models import *
import os
from flask import Flask, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flask.ext.login import current_user

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'upload')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['PROPAGATE_EXCEPTIONS'] = True

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

manager.create_api(Ad, methods=['GET', 'POST'])
manager.create_api(User, methods=['GET', 'POST'])
manager.create_api(Bid, methods=['GET', 'POST'])

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

	def allowed_file(filename):
		return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/cell_upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		ad = Ad(request.form['email'], request.form['price'], request.form['description'])
		db.session.add(ad)
		db.session.commit()
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(str(ad.id)+".jpg")
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return jsonify(path= os.path.join(app.config['UPLOAD_FOLDER'], filename))
	"""
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('uploaded_file',
									filename=filename))
	"""
	return '''
	<!doctype html>
	<title>Upload new File</title>
	<h1>Upload new File</h1>
	<form action="" method=post enctype=multipart/form-data>
	  <p><input type=file name=file>
	 <input type=number name=price>
	 <input type=text name=description>
	 <input type=email name=email>
		 <input type=submit value=Upload>
	</form>
	'''

@app.route("/")
def hello():
	return "Hello World!!!"

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated():
		return 'already logged in'
	if request.method == 'POST':
		user = request.form['user']
		password = request.form['password']
		return user + password
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
	app.run(host='0.0.0.0', port=8080, debug=True)
