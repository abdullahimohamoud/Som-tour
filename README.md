<<<<<<< HEAD
# Som-tour
A Python backend project that scrapes Somali tourist sites, geolocates them using GeoPy, and generates an interactive HTML map with Folium. It stores data in JSON or SQLite, highlighting Somalia’s beauty through automation and geospatial visualization.
=======
# Somalia Tourism Map Backend

This backend-only Python application scrapes online data about tourist attractions in Somalia, processes and geolocates the data, and generates an interactive map using Folium. The final output is a static HTML map showcasing Somalia’s tourism potential.

## Project Structure

```
som_tour_backend/
├── data/                  # Raw and processed data
│   └── attractions.json
├── maps/                  # Generated HTML maps
│   └── somalia_tourism_map.html
├── scraping/              # Web scraping logic
│   └── scraper.py
├── processing/            # Data cleaning and structuring
│   └── processor.py
├── geolocation/           # Geocoding logic
│   └── geolocator.py
├── mapping/               # Map generation logic
│   └── map_generator.py
├── main.py                # Main entry point
├── requirements.txt       # Python dependencies
└── README.md              # Project overview
```

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the pipeline:**
   ```bash
   python main.py
   ```
3. **View the map:**
   Open `maps/somalia_tourism_map.html` in your browser.

## What Each Module Does
- `scraping/scraper.py`: Scrapes Wikipedia for a list of Somali tourist attractions.
- `processing/processor.py`: Cleans and structures the scraped data.
- `geolocation/geolocator.py`: Geocodes each attraction using Nominatim.
- `mapping/map_generator.py`: Plots attractions on a Folium map.
- `main.py`: Orchestrates the workflow.

## Notes
- The scraper is a demo and may need adjustment for other sources.
- Geocoding uses free Nominatim API (rate-limited).
- No frontend or user interaction is required.

---

**Showcase Somalia’s tourism potential with a single command!**
>>>>>>> 9c60b67 (Initial commit: Somalia tourism backend project)
