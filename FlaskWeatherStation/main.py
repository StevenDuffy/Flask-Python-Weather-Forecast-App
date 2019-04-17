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

app.secret_key = os.urandom(24)

#user = None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:			
            return render_template('login.html', log_in_required=True)
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def login():
	return render_template('login.html')


@app.route("/login")
def logout():
	session.pop('user', None)
	#global user
	#user = None
	return redirect(url_for('login')) 

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


@app.route("/register", methods=['POST', 'GET'])
def register():
	return render_template('register.html')


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



