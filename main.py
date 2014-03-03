from config import db, app, manager, PORT
from models import *
from flask import jsonify
import test
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'upload')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

manager.create_api(Ad, methods=['GET', 'POST'])
manager.create_api(User, methods=['GET', 'POST'])
manager.create_api(Bid, methods=['GET', 'POST'])

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/cell_upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route("/")
def hello():
    return "Hello World!!!"

@app.route('/login')
def login():
	return 'enter a login'

@app.route('/create_testdb')
def create_testdb():
	db.create_all()
	return 'created tables'

@app.route('/delete_testdb')
def delete_testdb():
	bob = User.query.filter_by(first_name='bob').first()
	db.session.delete(bob)
	db.session.commit()
	return 'deleted tables'

@app.route('/user')
def get_user():
	users = [user.serialize() for user in User.query.all()]
	return jsonify(users=users)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
