from config import db, app, api_manager, PORT, login_manager
from models import *
import os
import zipfile 
from flask import Flask, request, redirect, url_for, jsonify, abort
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flask.ext.login import current_user, login_user, logout_user

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'upload')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/get_images')
def get_images():
	zipname = os.path.join(app.config['UPLOAD_FOLDER'], 'test.zip')
	zipf = zipfile.ZipFile(zipname, 'w')
	for i in range(0,10):
	filename = str(i) + ".jpg"
	filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
	zipf.write(filename)
	zipf.close()
	response = send_from_directory(app.config['UPLOAD_FOLDER'], 'test.zip')
	response.headers["Content-Disposition"] = "filename='test.zip'"
	return response


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
		return 'already logged in as %s' % current_user.get_id()
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		users = User.query.filter_by(email=email, password=password).all()
		if len(users) > 0:
			login_user(users[0])
			return '%s is logged in' % users[0].email
	return 'enter a login'

@app.route('/logout')
def logout():
	logout_user()
	return 'logged out'

@app.route('/create_testdb')
def create_testdb():
	db.create_all()
	return 'created tables'

@app.route('/user')
def get_user():
	users = [user.serialize() for user in User.query.all()]
	return jsonify(users=users)

@login_manager.user_loader
def load_user(id):
	return User.query.get(id)

@app.errorhandler(403)
def user_not_authenticated(error):
	return "user is not authenticated"

def auth_post(**kw):
	if request.method == 'POST':
		if not current_user.is_authenticated():
			abort(403)

def auth_both(**kw):
	if request.method == 'POST' or request.method == 'GET':
		if not current_user.is_authenticated():
			abort(403)

pre_auth_both = dict(GET_MANY=[auth_both], GET_SINGLE=[auth_both])
pre_auth_post = dict(GET_MANY=[auth_post], GET_SINGLE=[auth_post])
api_manager.create_api(Ad, methods=['GET', 'POST'], preprocessors=pre_auth_post)
api_manager.create_api(User, methods=['GET', 'POST'], preprocessors=pre_auth_post)
api_manager.create_api(Bid, methods=['GET', 'POST'], preprocessors=pre_auth_both)
api_manager.create_api(Message, methods=['GET', 'POST'], preprocessors=pre_auth_both)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
