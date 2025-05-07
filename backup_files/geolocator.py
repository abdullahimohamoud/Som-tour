# Made with love by @uncannystranger.
import json
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import time
import logging

def geolocate_attractions(input_path='data/attractions.json', output_path='data/attractions.json'):
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            attractions = json.load(f)
    except Exception as e:
        logging.error(f"Failed to load input data: {e}")
        return
    geolocator = Nominatim(user_agent="som_tourism_geolocator")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    for attr in attractions:
        if 'latitude' in attr and 'longitude' in attr and attr['latitude'] and attr['longitude']:
            continue  # Already geolocated
        query = f"{attr['name']}, {attr.get('location', 'Somalia')}"
        try:
            location = geocode(query)
            if location:
                attr['latitude'] = location.latitude
                attr['longitude'] = location.longitude
                logging.info(f"Geolocated: {attr['name']} -> ({location.latitude}, {location.longitude})")
            else:
                attr['latitude'] = None
                attr['longitude'] = None
                logging.warning(f"Could not geolocate: {attr['name']}")
        except Exception as e:
            attr['latitude'] = None
            attr['longitude'] = None
            logging.error(f"Error geolocating {attr['name']}: {e}")
            time.sleep(1)
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(attractions, f, ensure_ascii=False, indent=2)
        logging.info(f"Geolocated {len(attractions)} attractions.")
    except Exception as e:
        logging.error(f"Failed to write geolocated data: {e}")

def main():
    geolocate_attractions()

if __name__ == "__main__":
    main()
