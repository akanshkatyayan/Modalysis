# Modalysis: Cloud Computing Mini Project - Evaluate any Machine Learning Model
# -----------------------  imports ----------------------- #

from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired
import hashlib


# ----------------------- Web Forms Classes ----------------------- #

class LoginForm(FlaskForm):
	username = StringField(u'please enter your username:', validators=[DataRequired()])
	password = PasswordField(u'please enter your password:', validators=[DataRequired()])


# ----------------------- Initialize the app ----------------------- #

app = Flask(__name__)

# Landing page
@app.route('/')
def homepage():
	return render_template('templates/login.html')


# Login
@app.route('/login/', methods=['GET', 'POST'])
def login():
	login_form = LoginForm(request.form)
	if request.method == 'POST' and login_form.validate_on_submit():
		username = login_form.username.data
		password = login_form.password.data
		# again use hashing to check the password and authenticate
		# the hashing function always returns the same output for a given input,
		# so it can be used to check the password and api key
		u = username + password
		apikey = hashlib.sha256(u.encode('utf-8')).hexdigest()
		login_check=1
		#login_check = session.execute("""select COUNT(*) from journal.users where apikey='{}' ALLOW FILTERING""".format(apikey))
		if login_check == 1:
		# if login_check.was_applied == 1:
			return render_template('templates/dashboard.html', msg='successful!')
		else:
			return render_template('templates/login.html', msg_fail='failed! Wrong username or password 401')
	return render_template('templates/login.html', form=login_form)


# Dashboard


# ----------------------- Execute the app ----------------------- #

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
