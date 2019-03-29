#from urllib.request import urlopen
#import xml.etree.ElementTree as etree

import requests 
import datetime

def get_tomorrow_forecast():
	today = datetime.datetime.today()
	tomorrow = (today + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
	# Hard coded. Need to adjust and encode this.	
	weather_forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?APPID=8866dd7ea1284048f96667ab4b692c1c&q=Cambridge,UK&cnt=8&units=metric&dt_txt=' + tomorrow
	weather_forecast = requests.get(weather_forecast_url).json()	
	weatherobjects = []

	for three_hour_data in weather_forecast["list"]:
		weather_object = {"weather":"", "temperature":""}		
		weather_object["weather"] = three_hour_data["weather"][0]["main"]
		weather_object["temperature"] = three_hour_data["main"]["temp"]
		weatherobjects.append(weather_object)
			
	return weatherobjects 
	#forecast_date = weather_forecast["list"][3]["dt_txt"][2:10]
	# # API code for 3-5 day forecast is 8866dd7ea1284048f96667ab4b692c1c


# Original method that was in this file.
# 
#	bbcdic1= {
#	"daytype" : daytype_json ,
#	"weatherdescription" : weatherdescription_json,
#	"minimumtemperature" : minimumtemperature_json,
#	"maximumtemperature" : maximumtemperature_json
#	}