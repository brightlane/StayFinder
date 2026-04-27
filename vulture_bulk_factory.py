import csv
import random

# CONFIG
BASE_URL = "https://brightlane.github.io/SkyScanner/"
KEYWORDS_FILE = "keywords.txt" # Ensure this has your 1M nodes
OUTPUT_CSV = "vulture_bulk_social.csv"

# PSYCHOLOGICAL TRIGGERS
TEMPLATES = [
    "🚨 VULTURE ALERT: Mobile-only rates found for {city}! Genius T3 active.",
    "🏟️ 2026 WORLD CUP NODE: {city} inventory bypass online. Sniping now.",
    "🔥 RATE LEAK: {city} hotel markups extracted. Initialize snatch below.",
    "⚠️ SYSTEM SYNC: {city} nodes reporting 35% discount vs retail."
]

def generate_bulk_csv():
    with open(KEYWORDS_FILE, 'r') as f:
        cities = [line.strip() for line in f if line.strip()]

    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Headers for common bulk schedulers
        writer.writerow(["Content", "URL", "Schedule_Date"])
        
        for i, city in enumerate(cities):
            slug = city.lower().replace(" ", "-")
            url = f"{BASE_URL}?city={slug}"
            text = random.choice(TEMPLATES).format(city=city.upper())
            
            # This spreads 1,000,000 posts over time (Change logic as needed)
            writer.writerow([text, url, ""]) 

    print(f"✅ FACTORY COMPLETE: {len(cities)} rows ready in {OUTPUT_CSV}")

if __name__ == "__main__":
    generate_bulk_csv()
