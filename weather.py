import requests

RAPIDAPI_KEY = 'your_rapidapi_key_here'

def get_weather_by_ip(ip):
    # Определяем местоположение по IP
    location_url = "https://weatherapi-com.p.rapidapi.com/ip.json"
    location_querystring = {"q": ip}
    location_headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    location_response = requests.get(location_url, headers=location_headers, params=location_querystring)
    location_data = location_response.json()

    # Получаем погоду для определенного местоположения
    weather_url = "https://weatherapi-com.p.rapidapi.com/current.json"
    weather_querystring = {"q": location_data['city']}
    weather_headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    weather_response = requests.get(weather_url, headers=weather_headers, params=weather_querystring)
    weather_data = weather_response.json()

    # Формируем строку вывода
    weather_description = weather_data['current']['condition']['text']
    temperature = weather_data['current']['temp_c']
    location_city = location_data['city']
    location_country = location_data['country_name']
    output_string = f"In {location_city}, {location_country}: temperature: {temperature}, {weather_description}"
    return output_string
