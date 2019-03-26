from flask import Flask, render_template, url_for, flash, redirect
import requests 
import simplejson as json
import xml.etree.ElementTree as etree
from urllib.request import urlopen
from getweatherapi import *

#Tes
app = Flask(__name__)

# Connects to BBC weather and returns xml of Weather Data
def getbbcweather():
	weather_bbc = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/2653941'
	tree = etree.parse(urlopen(weather_bbc))
	return tree

#@app.home//
@app.route("/", methods=['GET', 'POST'])
def home():

	Weather = getweatherapi('Cambridge')

	return render_template('home.html', weather = Weather)

if __name__ == '__main__':
	app.run(debug='true')



