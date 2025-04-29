import requests
import os
from dotenv import load_dotenv

GEOCODING_API_URL = "https://maps.googleapis.com/maps/api/geocode/json"

load_dotenv()

def get_api_key():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set it in the .env file.")
    return api_key

def fetch_geocoding_data(place_name, api_key):
    parameters = {
        "address": place_name,
        "key": api_key
    }
    try:
        response = requests.get(GEOCODING_API_URL, params=parameters, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise ConnectionError(f"Error connecting to Geocoding API: {e}")

def parse_coordinates(data):
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        raise ValueError(f"Error from Geocoding API: {data['status']}")

def main():
    place = input("Enter the place name: ")
    try:
        api_key = get_api_key()
        data = fetch_geocoding_data(place, api_key)
        latitude, longitude = parse_coordinates(data)
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    except (ValueError, ConnectionError) as error:
        print(error)

if __name__ == "__main__":
    main()
