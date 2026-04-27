import requests
from bs4 import BeautifulSoup

def find_quora_targets(topic):
    # Quora is strict; this mimics a browser search
    search_url = f"https://www.google.com/search?q=site:quora.com+{topic}+2026+World+Cup+hotels"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    r = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if "quora.com" in str(href):
            links.append(href)
    
    return list(set(links))

# Example: Get targets for Dallas
targets = find_quora_targets("Dallas")
print(f"🎯 Target these high-intent questions: {targets}")
# 1. Load your 10k keywords
with open("keywords.txt", "r") as f:
    cities = [line.strip() for line in f if line.strip()]

# 2. Scout the top 10 cities for Quora targets
for city in cities[:10]: 
    print(f"--- Scouting Quora for {city} ---")
    targets = find_quora_targets(city)
    for t in targets:
        print(f"URL: {t}")
