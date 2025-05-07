# Made with love by @uncannystranger.
import json
import re
import logging

def clean_attractions(input_path='data/attractions.json', output_path='data/attractions.json'):
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            attractions = json.load(f)
    except Exception as e:
        logging.error(f"Failed to load input data: {e}")
        return
    cleaned = []
    seen = set()
    for attr in attractions:
        name = attr.get('name', '').strip()
        # Remove references in brackets (Wikipedia artifacts)
        name = re.sub(r'\[.*?\]', '', name)
        name = name.strip()
        desc = attr.get('description', '').strip()
        location = attr.get('location', 'Somalia').strip()
        if name and name.lower() not in seen:
            seen.add(name.lower())
            cleaned.append({
                'name': name,
                'description': desc,
                'location': location
            })
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(cleaned, f, ensure_ascii=False, indent=2)
        logging.info(f"Cleaned {len(cleaned)} attractions.")
    except Exception as e:
        logging.error(f"Failed to write cleaned data: {e}")

def main():
    clean_attractions()

if __name__ == "__main__":
    main()
