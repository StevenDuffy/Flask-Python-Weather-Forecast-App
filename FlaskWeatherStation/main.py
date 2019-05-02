from flask import Flask, render_template, url_for, flash, redirect, request, session, abort
import requests
import simplejson as json
from urllib.request import urlopen
from getforecast import get_forecast
import datetime
from database import database
from functools import wraps
import os
from hash import hash_string

app = Flask(__name__)

# Genrates a secret key to encrypt session data with.
app.secret_key = os.urandom(24)

#user = None

# Decorator wraps endpoints that require the user to be logged in and blocks access if not logged in. 
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:			
            return render_template('login.html', log_in_required=True)
        return f(*args, **kwargs)
    return decorated_function

# Root endpoint presents login page. 
@app.route("/")
def login():
	return render_template('login.html')

# Endpoint used when user logs out. Removes session.
@app.route("/login")
def logout():
	session.pop('user', None)
	#global user
	#user = None
	return redirect(url_for('login')) 

# Endpoint for users registering. Sends user to login page if successful or advises user
# they already exist.
@app.route("/registered/login" , methods=['POST', 'GET'])
def register_user():
	dataconn = database()
	if request.method == 'POST':
		credentials = {}
		credentials["first_name"] = request.form.get('firstName')
		credentials["second_name"] = request.form.get('secondName')
		credentials["username"] = request.form.get('username')
		credentials["password"] = hash_string(request.form.get('psw'))
		if (dataconn.check_username_exists(credentials)):
			dataconn.close()
			return render_template("register.html", user_exists=True)
		else:
			dataconn.add_user(credentials)
			dataconn.close()
			return render_template("login.html", registration_succeeded=True)
	else:
		abort(403)

# Endpoint directs user to register page.
@app.route("/register", methods=['POST', 'GET'])
def register():
	return render_template('register.html')

# Successful login presents home page. Failed login directs user to login page with 
# invalid credentials message.
@app.route("/home", methods=['POST', 'GET'])
def home():
	dataconn = database()
	if request.method == 'POST':
		credentials = {}
		credentials["username"] = request.form.get('username')
		credentials["password"] = hash_string(request.form.get('psw'))
		if (dataconn.verify_user(credentials)):
			dataconn.close()
			session['user'] = credentials["username"]			
			#global user 
			#user = credentials
			return render_template('home.html')
		else:
			return render_template('login.html', invalid_credentials=True)
	else:
		return render_template('login.html', log_in_required=True )

# Gets three-day weather data for the submitted location and generates this on the home 
# page. If data is not found, the home page is generated with a location not found message.
@app.route("/locationforecast", methods=['GET','POST'])
@login_required
def location_next_day_forecast():
	location = request.args.get("location")
	try:
		weather_data_one = get_forecast(location, 1)
		weather_data_two = get_forecast(location, 2)
		weather_data_three = get_forecast(location, 3)
		return render_template('home.html', weather_data_one=weather_data_one,weather_data_two=weather_data_two,weather_data_three=weather_data_three)
	except:		
		#return redirect(url_for('next_day_forecast', location=False))
		return render_template('home.html', error = True)


if __name__ == '__main__':
	app.run(debug='true')



