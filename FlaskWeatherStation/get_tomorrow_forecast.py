#from urllib.request import urlopen
#import xml.etree.ElementTree as etree
import requests 
import datetime

def get_tomorrow_forecast():
	weather_forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?APPID=8866dd7ea1284048f96667ab4b692c1c&q=Manchester,UK'
	weather_forecast = requests.get(weather_forecast_url).json()

	today = datetime.datetime.today()
	tomorrow = (today + datetime.timedelta(days=1)).strftime("%y-%m-%d")

	forecast_date = weather_forecast["list"][0]["dt_txt"]
	forecast_date2 = forecast_date[0:11]
	 
	


	return forecast_date2

# API code for 3-5 day forecast is 8866dd7ea1284048f96667ab4b692c1c



# 
#	bbcdic1= {
#	"daytype" : daytype_json ,
#	"weatherdescription" : weatherdescription_json,
#	"minimumtemperature" : minimumtemperature_json,
#	"maximumtemperature" : maximumtemperature_json
#	}