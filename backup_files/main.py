# Made with love by @uncannystranger.
import logging
from scraping.scraper import scrape_attractions
from processing.processor import clean_attractions
from geolocation.geolocator import geolocate_attractions
from mapping.map_generator import generate_map

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Somalia Tourism Map pipeline...")
    scrape_attractions()
    clean_attractions()
    geolocate_attractions()
    generate_map()
    logging.info("Pipeline complete. Check maps/somalia_tourism_map.html.")

if __name__ == "__main__":
    main()
