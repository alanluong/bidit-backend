from flask import Flask
app = Flask(__name__)

@app.route("/login")
def login():
	if request.method == 'POST':
		pass
	else:
		return "enter a login"


if __name__ == "__main__":
	app.run()
