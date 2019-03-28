from urllib.request import urlopen
import requests 



def getweatherapi(Location):
	Weather_api = 'https://api.openweathermap.org/data/2.5/weather?APPID=89da9ee78fce51911e8ca20b9906d704&q='
	# Address+Location Returns location relevant data
	User_Weather_api = Weather_api + Location
	#Resposne Request Returned as .Json file
	Weather = requests.get(User_Weather_api).json()

	weather_type_json = Weather['weather'][0]['main']          
	tempreture_json = float(Weather['main']['temp'])
	
	weatherapidic = {
	"weathertype" : weather_type_json ,
	"tempreture" : tempreture_json
	}

	return weatherapidic

#8866dd7ea1284048f96667ab4b692c1c