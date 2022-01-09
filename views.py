import requests
from django.shortcuts import render
from weather.models import City
# Create your views here.
def home(request):
    if request.method == 'POST':
        nameOfCity = request.POST['cityName']
        named = City(name=nameOfCity)
        named.save()
    # city = 'los angeles'
    cities = City.objects.all()
    weather_data = []
    # print(cities)
    # url = f'https://api.openweathermap.org/data/2.5/onecall? timezone={city}&lat=33.44&lon=-94.04&exclude=hourly,daily&appid=591c974f883a2b63573b7cc8f4b87715'
    for place in cities:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&APPID=591c974f883a2b63573b7cc8f4b87715'
        responseOfWeather = requests.get(url.format(place)).json()
        # print(responseOfWeather)

        city_weatherMap = {
            'city':place,
            'temperature':responseOfWeather['main']['temp'],
            'description':responseOfWeather['weather'][0]['description'],
            'icon': responseOfWeather['weather'][0]['icon'],

        }
        weather_data.append(city_weatherMap)
    # print(city_weatherMap)
    print(weather_data)
    context = {'weather_data':weather_data}
    return render(request,'weather.html',context)