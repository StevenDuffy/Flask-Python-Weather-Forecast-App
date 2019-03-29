from flask import Flask, render_template, url_for, flash, redirect, request
import requests
import simplejson as json
import xml.etree.ElementTree as etree
from urllib.request import urlopen
from getweatherapi import *
from get_tomorrow_forecast import get_tomorrow_forecast
import datetime


app = Flask(__name__)

#   Connects to BBC weather and returns xml of Weather Data
#	weather_bbc = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/2653941'
#	tree = etree.parse(urlopen(weather_bbc))
#	return tree


@app.route("/", methods=['GET'])
def next_day_forecast():

	#weather_data = get_tomorrow_forecast("Falkirk")
	weather_data = None
	return render_template('home.html', weather_data=weather_data)


@app.route("/location", methods=['GET'])
def location_next_day_forecast():
	location = request.args.get("location")
	try:
		weather_data = get_tomorrow_forecast(location)
		return render_template('home.html', weather_data=weather_data)
	except:
		# Need to generate the error message for the user.
		# return redirect(url_for('next_day_forecast', location=False))
		return render_template('home.html', weather_data=None, error = False)

# Original method. Gets current weather so will likely be used for the index page.
# @app.route("/", methods=['GET', 'POST'])


def home():
	Weather = getweatherapi('Cambridge')
	return render_template('home.html', weather=Weather)

# Original html, I had to remove it from home.html temporarily to test other features.
# <p> According to WeatherApi.com:	</p>
# <p> Weather: {{weather.weathertype}} </p>
# <p> Temp: {{weather.tempreture}} K </p>


if __name__ == '__main__':
	app.run(debug='true')
