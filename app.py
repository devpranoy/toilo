from flask import Flask ,render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import dbquery

app = Flask(__name__)
def is_logged_in(f):	# Function for implementing security and redirection
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Unauthorised, Please Login')
			return redirect(url_for('login'))
	return wrap	# A wrap is a concept that is used to check for authorisation of a request


@app.route('/dashboard',methods=['GET','POST'])
@is_logged_in	
def dashboard():
	return render_template('dashboard.html')

@app.route('/login', methods=['GET','POST']) #login page
def login():
	if request.method == 'POST':
		email = request.form['email']					#GET FORM FIELDS
		password_candidate= request.form['password']	#GET FORM FIELDS
		flag=0
		

		sql="SELECT PASSWORD FROM USERS WHERE EMAIL= '%s' "%(email)
		rows = dbquery.fetchone(sql)
		try:				# if no entry found, an error is raised
			for row in rows:
				flag=1
				password=row
			sql="SELECT NAME FROM USERS WHERE EMAIL= '%s' "%(email)		#validations
			rows = dbquery.fetchone(sql)
			for row in rows:
				name=row
			sql="SELECT USERID FROM USERS WHERE EMAIL= '%s' "%(email)	#validations
			rows = dbquery.fetchone(sql)
			for row in rows:
				userid=row
			
			for row in rows:
				city=row
			if str(password_candidate) == str(password):	#initialise session variable if passwords match
				session['logged_in'] = True
				session['name'] = str(name)
				session['userid']=userid
			
                
			else:
				error = 'Invalid login'
				return render_template('login.html',error=error)
		except:
			if flag==0:
				error = 'Email not found'
				return render_template('login.html',error=error)
		return redirect(url_for('dashboard'))#if verification is successful load the dashboard with session
	return render_template('login.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
	if request.method == 'POST':
		email = request.form['email']					#GET FORM FIELDS
		password_candidate= request.form['password']
		name = request.form['name']
		sql="SELECT USERID FROM USERS WHERE EMAIL='%s'"%(email) #Security check on email
		try:
			rows = dbquery.fetchone(sql) #if none, error should be raised
			for row in rows:
				f=1
		except:
			sql="INSERT INTO USERS(NAME,EMAIL,PASSWORD) VALUES('%s','%s' ,'%s')"%(name,email,password_candidate)
			dbquery.inserttodb(sql)	#connecting to db model
			flash('You are now registered! Please Log in.','success') #sending a message to user
			return redirect(url_for('login')) #redirecting to login page
		flash('This Email exists!','success') #Checking for email
		return render_template('signup.html')
	return render_template('signup.html')

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('index.html')

if __name__=='__main__':
	app.secret_key='secret123' #for flash messaging
	app.run(host='0.0.0.0',port =80,debug=True) #Debugger is set to 1 for testing and overriding the default port to http port
