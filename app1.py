from flask import Flask ,render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import dbquery

app = Flask(__name__)
@app.route('/')		#main route
def index():		#index page
	return render_template('index.html')

if __name__=='__main__':
	app.secret_key='secret123' #for flash messaging
	app.run(host='0.0.0.0',port =80,debug=True) #Debugger is set to 1 for testing and overriding the default port to http port
