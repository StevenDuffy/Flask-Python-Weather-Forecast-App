#from urllib.request import urlopen
#import xml.etree.ElementTree as etree

import requests
import datetime
import urllib


def get_tomorrow_forecast(Location):
	today = datetime.datetime.today()
	tomorrow = (today + datetime.timedelta(days=1)).strftime("%y-%m-%d")
	# Hard coded. Need to adjust and encode this.
	# urllib.parse.urlencode()
	weather_forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?APPID=8866dd7ea1284048f96667ab4b692c1c&q=' + \
		Location + ',UK&cnt=16&units=metric'
	weather_forecast = requests.get(weather_forecast_url).json()
	weatherobjects = []

	for three_hour_data in weather_forecast["list"]:
		if three_hour_data["dt_txt"][2:10] == tomorrow:
			weather_object = {"weather": "", "temperature": ""}
			weather_object["weather"] = three_hour_data["weather"][0]["main"]
			weather_object["temperature"] = three_hour_data["main"]["temp"]
			weatherobjects.append(weather_object)

	return weatherobjects

	# API code for 3-5 day forecast is 8866dd7ea1284048f96667ab4b692c1c
	# forecast_date = weather_forecast["list"][8]["dt_txt"][2:10]

# Original method that was in this file.
#
#	bbcdic1= {
#	"daytype" : daytype_json ,
#	"weatherdescription" : weatherdescription_json,
#	"minimumtemperature" : minimumtemperature_json,
#	"maximumtemperature" : maximumtemperature_json
#	}
