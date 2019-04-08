from flask import Flask, render_template, url_for, flash, redirect, request
import requests
import simplejson as json
#import xml.etree.ElementTree as etree
from urllib.request import urlopen
#from getweatherapi import *
from getforecast import get_forecast
import datetime
from database import database


app = Flask(__name__)

@app.route("/")
def Login():
	return render_template('login.html')


@app.route("/home", methods=['POST', 'GET'])
def Home():
	dataconn = database()
	if request.method == 'POST':
		credentials = {}
		credentials["username"] = request.form.get('username')
		credentials["password"] = request.form.get('psw')
		if (dataconn.verify_user(credentials)):
			return render_template('home.html')
		else:
			return render_template('login.html', invalid_credentials=True)
	else:
		return render_template('login.html', logged_out=True) # add an error message here for invalid credentials


@app.route("/locationforecast", methods=['GET'])
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

#def home_original():
#	Weather = getweatherapi('Cambridge')
#	return render_template('home.html', weather=Weather)

#   Connects to BBC weather and returns xml of Weather Data
#	weather_bbc = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/2653941'
#	tree = etree.parse(urlopen(weather_bbc))
#	return tree

# Original html, I had to remove it from home.html temporarily to test other features.
# <p> According to WeatherApi.com:	</p>
# <p> Weather: {{weather.weathertype}} </p>
# <p> Temp: {{weather.tempreture}} K </p>


if __name__ == '__main__':
	app.run(debug='true')
