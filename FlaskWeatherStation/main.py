from flask import Flask, render_template, url_for, flash, redirect
import requests 
import simplejson as json
import xml.etree.ElementTree as etree
from urllib.request import urlopen
from getweatherapi import *
from get_three_day_forecast import get_three_day_forecast
import datetime


app = Flask(__name__)

#   Connects to BBC weather and returns xml of Weather Data
#
#	weather_bbc = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/2653941'
#	tree = etree.parse(urlopen(weather_bbc))
#	return tree

#@app.home//
@app.route("/", methods=['GET', 'POST'])
def three_day_forecast():
	# forecast = get_bbc_weather() 
	date = (datetime.datetime.today()).strftime("%y-%m-%d")
	#date2 = (date1 + datetime.timedelta(200000)).strftime("%y-%m-%d")
	
	return render_template('home.html', date=date)

# Original method. Gets current weather so will likely be used for the index page . 
# 
#def home():
#	Weather = getweatherapi('Cambridge')
#	return render_template('home.html', weather = Weather)

# Original html, I had to move it temporarily.
# <p> According to WeatherApi.com:	</p>
# <p> Weather: {{weather.weathertype}} </p>
# <p> Temp: {{weather.tempreture}} K </p>

if __name__ == '__main__':
	app.run(debug='true')


