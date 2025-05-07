# Made with love by @uncannystranger.
import json
from bs4 import BeautifulSoup
import requests
import logging

WIKIVOYAGE_URL = "https://en.wikivoyage.org/wiki/Somalia"

logging.basicConfig(level=logging.INFO)

def scrape_attractions():
    try:
        response = requests.get(WIKIVOYAGE_URL, timeout=10)
        response.raise_for_status()
    except Exception as e:
        logging.error(f"Failed to fetch Wikivoyage page: {e}")
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    attractions = []
    # Look for attractions in the 'See' section
    see_header = soup.find(['span', 'h2', 'h3'], string=lambda s: s and 'See' in s)
    if see_header:
        # Find the next ul after the 'See' header
        ul = see_header.find_parent().find_next_sibling('ul')
        if ul:
            for li in ul.find_all('li', recursive=False):
                name = li.get_text(strip=True)
                desc = ''
                desc_tag = li.find(['i', 'small'])
                if desc_tag:
                    desc = desc_tag.get_text(strip=True)
                if name:
                    attractions.append({
                        'name': name,
                        'description': desc,
                        'location': 'Somalia'
                    })
    if not attractions:
        logging.warning("No attractions found. Wikivoyage structure may have changed.")
    try:
        with open('data/attractions.json', 'w', encoding='utf-8') as f:
            json.dump(attractions, f, ensure_ascii=False, indent=2)
        logging.info(f"Scraped {len(attractions)} attractions.")
    except Exception as e:
        logging.error(f"Failed to write data: {e}")

if __name__ == "__main__":
    scrape_attractions()
