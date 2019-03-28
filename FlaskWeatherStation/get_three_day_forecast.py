#from urllib.request import urlopen
#import xml.etree.ElementTree as etree
import requests 


def get_three_day_forecast():
	weather_forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?APPID=8866dd7ea1284048f96667ab4b692c1c&q=Manchester,UK'
	weather_forecast = requests.get(weather_forecast_url).json()
	date = (datetime.datetime.today()).strftime("%y-%m-%d")
	#date2 = (date1 + datetime.timedelta(200000)).strftime("%y-%m-%d")
	return weather_forecast

# API code for 3-5 day forecast is 8866dd7ea1284048f96667ab4b692c1c



# 
#	bbcdic1= {
#	"daytype" : daytype_json ,
#	"weatherdescription" : weatherdescription_json,
#	"minimumtemperature" : minimumtemperature_json,
#	"maximumtemperature" : maximumtemperature_json
#	}