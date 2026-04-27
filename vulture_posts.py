import random
import json

# 1. CONFIGURATION
BASE_URL = "https://brightlane.github.io/SkyScanner/"
KEYWORDS_FILE = "keywords.txt" # Your list of 10k-1M cities
OUTPUT_FILE = "vulture_social_payload.txt"

# 2. THE PSYCHOLOGICAL TRIGGER MATRIX (Copy Spinning)
HOOKS = [
    "🚨 INVENTORY LEAK:", "⚠️ SYSTEM BYPASS:", "🦅 VULTURE ALERT:", 
    "🔥 RATE DROP:", "🏟️ 2026 STADIUM UPDATE:", "💎 SECRET RATES:"
]

MESSAGES = [
    "Extracted Mobile-Only rates for {city}. Genius Tier 3 active.",
    "Bypassing retail markups for {city} hotels. Inventory sniper online.",
    "Direct-to-inventory access opened for {city}. Sniping 30-40% off.",
    "Stadium Node {city} just synced. Extreme discounts detected.",
    "Found secret hotel inventory for {city}. Mobile users only."
]

CTAS = [
    "Initialize Snatch here: {url}",
    "Secure Node Access: {url}",
    "Bypass Retail Here: {url}",
    "Extract Rate: {url}",
    "View Leaked Rates: {url}"
]

TAGS = " #WorldCup2026 #TravelHacks #VultureProtocol #HotelDeals"

def generate_social_swarm():
    try:
        with open(KEYWORDS_FILE, 'r') as f:
            cities = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        cities = ["Dallas", "Miami", "London", "Tokyo"] # Seed if file is missing

    payload = []

    for city in cities:
        # Create the SEO-clean URL
        slug = city.lower().replace(" ", "-")
        target_url = f"{BASE_URL}?city={slug}"
        
        # Spin the content
        hook = random.choice(HOOKS)
        msg = random.choice(MESSAGES).format(city=city.upper())
        cta = random.choice(CTAS).format(url=target_url)
        
        post = f"{hook} {msg}\n{cta}\n{TAGS}\n{'-'*30}"
        payload.append(post)

    with open(OUTPUT_FILE, 'w') as f:
        f.write("\n".join(payload))
    
    print(f"✅ SWARM READY: {len(payload)} posts generated in {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_social_swarm()
