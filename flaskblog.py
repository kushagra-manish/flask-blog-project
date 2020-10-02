from flask import Flask, url_for
from forms import RegistrationForm, LoginForm

import flask
app = Flask(__name__)

app.config['SECRET_KEY'] = "4a55519fea8ef88963f795077afa3691"
posts=[
	{"author":"Kushagra Manish","date_posted":"2nd April,2020","title":"Hello There","content":"General Kenobi"},
	{"author":"Kushagra Manish","date_posted":"2nd April,2020","title":"Hello There","content":"General Kenobi"},
]
@app.route("/")
@app.route("/home")
def hello():
	return flask.render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return flask.render_template("about.html" ,title = 'about' )

@app.route("/register")
def register():
	form = RegistrationForm()
	return flask.render_template("register.html" ,title = 'Register' , form = form)

@app.route("/login")
def login():
	form = LoginForm()
	return flask.render_template("login.html" ,title = 'Login' , form = form)


if __name__ == "__main__":
	app.run(debug=True)