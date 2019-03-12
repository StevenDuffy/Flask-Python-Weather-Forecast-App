from flask import Flask, render_template, url_for, flash, redirect
import requests 
import simplejson as json
import xml.etree.ElementTree as etree
from urllib.request import urlopen


app = Flask(__name__)

# Connects to weatherapi.com and returns json of Weather Data
def getweatherapi(Location):
	
	Weather_api ='https://api.openweathermap.org/data/2.5/weather?APPID=89da9ee78fce51911e8ca20b9906d704&q='
	# Address+Location Returns location relevant data
	User_Weather_api = Weather_api + Location
	#Resposne Request Returned as .Json file 
	Weather = requests.get(User_Weather_api).json()
	return Weather

# Connects to BBC weather and returns xml of Weather Data
def getbbcweather():
	weather_bbc = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/2653941'
	tree = etree.parse(urlopen(weather_bbc))
	return tree

#Method:Random Activity Return: Activity



#Method: Sorts Dictionary Variables Return: Variable 


#@app.home//
@app.route("/", methods=['GET', 'POST'])
def home():

	Weather = getweatherapi('Cambridge')
	weather_type = Weather['weather'][0]['main']
	tempreture = float(Weather['main']['temp'])


	return render_template('home.html', title = 'home', weather_type = weather_type, tempreture=tempreture)

if __name__ == '__main__':
	app.run(debug='true')



