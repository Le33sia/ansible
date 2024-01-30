
import requests
import argparse

def get_weather(api_key, city):
    api_url = "http://api.weatherstack.com/current"
    params = {'access_key': api_key, 'query': city}

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
	return None

def main():
    parser = argparse.ArgumentParser(description='Get weather information from Weathe>
    
    # Optional command-line arguments
    parser.add_argument('--api-key', help='Weatherstack API key')
    parser.add_argument('--city', help='City name for weather information')

    args = parser.parse_args()

    # Set default values or read from command-line arguments
    api_key = '891e8c047d792a1f405de9baf6cb6ef4'  # Replace with your actual Weathers>
    city = args.city  # Default city is London

    weather_data = get_weather(api_key, city)

    if weather_data:
        try:
            temperature = weather_data['current']['temperature']
            description = weather_data['current']['weather_descriptions'][0]
            print(f"Weather in {city}: {temperature}°C, {description}")
        except KeyError as e:
            print(f"Unexpected response format. KeyError: {e}")
            print("Full response:", weather_data)
    else:
	print("API Call Failed. Full response:", weather_data)

if __name__ == "__main__":
    main()

