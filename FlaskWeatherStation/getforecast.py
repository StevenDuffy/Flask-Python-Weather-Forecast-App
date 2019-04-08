#from urllib.request import urlopen
#import xml.etree.ElementTree as etree

import requests
import datetime
import urllib


def get_forecast(location, days_to_add):
	today = datetime.date.today()
	tomorrow = (today + datetime.timedelta(days= days_to_add)).strftime("%y-%m-%d")
	# Hard-coded. Need to adjust and encode this.
	# urllib.parse.urlencode()
	weather_forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?APPID=8866dd7ea1284048f96667ab4b692c1c&q=' + \
		location + ',UK&cnt=40&units=metric'

	weather_forecast = requests.get(weather_forecast_url).json()

	weatherobjects = []

	for three_hour_data in weather_forecast["list"]:
		if three_hour_data["dt_txt"][2:10] == tomorrow:
			weather_object = {}
			weather_object["weather"] = three_hour_data["weather"][0]["main"]
			weather_object["temperature"] = float(three_hour_data["main"]["temp"]).__round__()
			weather_object["date"] = three_hour_data["dt_txt"][0:10]
			weather_object["time"] = three_hour_data["dt_txt"][10:16]
			weatherobjects.append(weather_object)

	return weatherobjects

# Original method that was in this file.
#
#	bbcdic1= {
#	"daytype" : daytype_json ,
#	"weatherdescription" : weatherdescription_json,
#	"minimumtemperature" : minimumtemperature_json,
#	"maximumtemperature" : maximumtemperature_json
#	}
