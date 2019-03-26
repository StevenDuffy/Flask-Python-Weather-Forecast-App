from urllib.request import urlopen
import requests 
import simplejson as json

def getbbcweather():
	weather_bbc = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/2653941'
	tree = etree.parse(urlopen(weather_bbc))
	return tree


	bbcdic1= {
	"daytype" : daytype_json ,
	"weatherdescription" : weatherdescription_json,
	"minimumtemperature" : minimumtemperature_json,
	"maximumtemperature" : maximumtemperature_json
	}