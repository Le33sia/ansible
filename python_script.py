import requests
import argparse
import configparser
from getpass import getpass

def get_weather(api_key, city):
    api_url = "http://api.weatherstack.com/current"
    params = {'access_key': api_key, 'query': city}

    response = requests.get(api_url, params=params)

    return response.json() if response.status_code == 200 else None

def load_config():
    config = configparser.ConfigParser()
    try:
        config.read('config.ini')
        return config['WeatherConfig']
    except configparser.Error:
        print("Error reading config file. Using default values.")
        return {}

def get_api_key():
    # Prompt user for API key securely
    api_key = getpass("Enter Weatherstack API key: ")
    return api_key

def parse_arguments():
    parser = argparse.ArgumentParser(description='Get weather information from Weatherstack API')

    parser.add_argument('--api-key', help='Weatherstack API key')
    parser.add_argument('--city', help='City name for weather information')

    return parser.parse_args()

def main():
    args = parse_arguments()

    # Load default values from config file
    config = load_config()
    api_key = args.api_key or config.get('api_key') or get_api_key()
    city = args.city or config.get('default_city')

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
