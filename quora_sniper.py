import requests
from bs4 import BeautifulSoup
import time
import csv

# 1. TARGETING CONFIG
TARGET_NODES = ["Dallas World Cup", "Miami 2026 Hotels", "Monterrey Estadio BBVA", "New York MetLife Stay"]
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
OUTPUT_FILE = "quora_targets.csv"

def scout_quora(topic):
    """Interrogates Google to find high-authority Quora nodes."""
    print(f"📡 SCANNING NODE: {topic}...")
    
    # site:quora.com forces the search to only return Quora threads
    search_query = f"https://www.google.com/search?q=site:quora.com+{topic.replace(' ', '+')}+2026+hotels"
    
    try:
        response = requests.get(search_query, headers={'User-Agent': USER_AGENT})
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = []
        # Google search results are usually in 'a' tags within 'div.g' or similar structures
        for a in soup.find_all('a', href=True):
            url = a['href']
            if "quora.com/" in url and "google.com" not in url:
                # Clean the URL from Google redirect parameters
                clean_url = url.split('&')[0].replace('/url?q=', '')
                links.append(clean_url)
        
        return list(set(links)) # Remove duplicates
    except Exception as e:
        print(f"❌ RECON FAILED for {topic}: {e}")
        return []

def main():
    print("🦅 VULTURE QUORA SNIPER INITIALIZED...")
    all_targets = []

    for node in TARGET_NODES:
        results = scout_quora(node)
        for link in results:
            all_targets.append([node, link])
        # Stealth delay to avoid Google's "Anti-Vulture" rate limiting
        time.sleep(2)

    # 2. SAVE THE INTELLIGENCE
    with csv.writer(open(OUTPUT_FILE, "w", newline='')) as f:
        f.writerow(["Node", "Quora_Thread_URL"])
        f.writerows(all_targets)

    print(f"✅ RECON COMPLETE: {len(all_targets)} targets saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
