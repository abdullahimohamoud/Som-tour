# Made with love by @uncannystranger.
import json
import folium
import logging

def generate_map(input_path='data/attractions.json', output_path='maps/somalia_tourism_map.html'):
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            attractions = json.load(f)
    except Exception as e:
        logging.error(f"Failed to load geolocated data: {e}")
        return
    somalia_center = [5.1521, 46.1996]
    m = folium.Map(location=somalia_center, zoom_start=6, tiles='CartoDB positron')
    count = 0
    for attr in attractions:
        lat = attr.get('latitude')
        lon = attr.get('longitude')
        if lat is not None and lon is not None:
            folium.Marker(
                location=[lat, lon],
                popup=f"<b>{attr['name']}</b><br>{attr.get('description', '')}",
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(m)
            count += 1
    if count == 0:
        logging.warning("No valid geolocated attractions to plot on the map.")
    try:
        m.save(output_path)
        logging.info(f"Map generated with {count} attractions at {output_path}.")
    except Exception as e:
        logging.error(f"Failed to save map: {e}")

def main():
    generate_map()

if __name__ == "__main__":
    main()
