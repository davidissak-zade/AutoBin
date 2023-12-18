import requests

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
API_KEY = '714cbe6a5a2bf70b9534c6e65cf927ba'

# Replace 'YOUR_CITY_NAME' with the name of your city
CITY = 'Haifa, Israel'

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Build the URL for the API request
url = f'{BASE_URL}?q={CITY}&appid={API_KEY}'

# Send a GET request to the API
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Extract relevant weather information
temperature = data['main']['temp']
humidity = data['main']['humidity']
description = data['weather'][0]['description']

# Print the weather information
print(f'Temperature: {temperature} K')
print(f'Humidity: {humidity}%')
print(f'Description: {description}')
