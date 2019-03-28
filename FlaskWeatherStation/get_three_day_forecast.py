#from urllib.request import urlopen
#import xml.etree.ElementTree as etree
import requests 


def get_three_day_forecast():
	weather_forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?APPID=8866dd7ea1284048f96667ab4b692c1c&q=Manchester,UK'
	weather_forecast = requests.get(weather_forecast_url).json()
	return weather_forecast





# 
#	bbcdic1= {
#	"daytype" : daytype_json ,
#	"weatherdescription" : weatherdescription_json,
#	"minimumtemperature" : minimumtemperature_json,
#	"maximumtemperature" : maximumtemperature_json
#	}