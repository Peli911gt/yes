import requests

# API key for OpenWeatherMap
api_key = '75c302539fddd53d07ce2fcda119eddb'

# Base URL for the OpenWeatherMap API
base_url = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city):
    # Construct the URL with the API key and city name
    url = f'{base_url}?q={city}&appid={api_key}'

    try:
        # Send the GET request to the API
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the weather data from the JSON response
            weather_data = response.json()
            return weather_data
        else:
            # Display an error message if the request was unsuccessful
            print(f'Error: {response.status_code} - {response.text}')
    except requests.exceptions.RequestException as e:
        # Display an error message if there was a network-related error
        print(f'Error: {e}')

# Example usage
city_name = 'London'
data = get_weather_data(city_name)
print(data)
