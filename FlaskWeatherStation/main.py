from flask import Flask, render_template, url_for, flash, redirect, request
import requests
import simplejson as json
#import xml.etree.ElementTree as etree
from urllib.request import urlopen
#from getweatherapi import *
from getforecast import get_forecast
import datetime
from database import database
from functools import wraps


app = Flask(__name__)

user = None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if user == None:			
            return render_template('login.html', logged_out=True)
        return f(*args, **kwargs)
    return decorated_function



@app.route("/")
def Login():
	return render_template('login.html')

@app.route("/logout")
def Logout():
	global user
	user = None
	return redirect(url_for('Login')) 



@app.route("/home", methods=['POST', 'GET'])
def Home():
	dataconn = database()
	if request.method == 'POST':
		credentials = {}
		credentials["username"] = request.form.get('username')
		credentials["password"] = request.form.get('psw')
		if (dataconn.verify_user(credentials)):
			global user 
			user = credentials
			return render_template('home.html')
		else:
			return render_template('login.html', invalid_credentials=True)
	else:
		return render_template('home.html') # add an error message here for invalid credentials


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
		# return redirect(url_for('next_day_forecast', location=False))
		return render_template('home.html', error = True)


if __name__ == '__main__':
	app.run(debug='true')



