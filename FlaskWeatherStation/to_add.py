# Add to home.html 
# This is day two
{% if weather_data_two %}
  <div class="container alignment" id="row2">
    <div class="row">
      {% for data in weather_data_two %}
      <div class="col-sm mycol">
        <h6>{{data.time}}</h6>
        <img>
        <p class="weather">{{data.weather}}</p>
        <p>{{data.temperature}}<sup>o</sup>C</p>
      </div>
      {% endfor %}
      {% endif %}
    </div>
  </div>

# Add to home.html 
# This is day three

  {% if weather_data_three %}
  <div class="container alignment" id="row3">
    <div class="row">
      {% for data in weather_data_three %}
      <div class="col-sm">
        <h6>{{data.time}}</h6>
        <img>
        <p class="weather">{{data.weather}}</p>
        <p>{{data.temperature}}<sup>o</sup>C</p>
      </div>
      {% endfor %}
      {% endif %}
    </div>
  </div>

###############  add to main.py under - location_next_day_forecast():
#This is day two
weather_data_two = get_tomorrow_forecast(location, 2)
# Add this parameter to be sent in the render template
, weather_data_two=weather_data_two

#This is day three
weather_data_three = get_tomorrow_forecast(location, 3)
# Add this parameter to be sent in the render template
, weather_data_three=weather_data_three
