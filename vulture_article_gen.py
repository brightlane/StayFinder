import os

# 1. SETUP
KEYWORDS_FILE = 'keywords.txt'
BASE_URL = 'https://brightlane.github.io/SkyScanner/'

# 2. THE CONTENT SPINNER (Multi-variant templates to avoid footprint)
TEMPLATES = [
    """<h2>2026 Inventory Report: {city}</h2>
    <p>The global housing matrix for 2026 is tightening. In {city}, we are seeing a massive surge in direct-to-inventory requests. 
    By bypassing the standard retail markup layers, travelers can currently access mobile-only Genius Tier 3 rates.</p>
    <p><strong>Pro Tip:</strong> The stadium district in {city} is currently under a high-intensity booking block. 
    Use the Vulture Matrix to snipe secondary market inventory before the public release.</p>""",
    
    """<h2>Sniper Alert: {city} Stadium District</h2>
    <p>Our AI nodes have detected a price drop in {city}. While retail platforms show 'Sold Out' for major 2026 dates, 
    the direct-to-inventory layer still shows availability for those with the correct node access.</p>
    <p>Accessing {city} via the Vulture Protocol ensures you are not paying the 25% 'Aggregator Tax' typically added by travel agencies.</p>"""
]

def generate_articles():
    if not os.path.exists(KEYWORDS_FILE):
        print("❌ keywords.txt missing.")
        return

    with open(KEYWORDS_FILE, 'r') as f:
        cities = [line.strip() for line in f if line.strip()]

    print(f"🦅 GENERATING {len(cities)} ARTICLES...")

    for i, city in enumerate(cities):
        slug = city.lower().replace(" ", "-")
        node_path = f"nodes/{slug}"
        os.makedirs(node_path, exist_ok=True)

        content = TEMPLATES[i % len(TEMPLATES)].format(city=city)

        # BUILD THE SEO LANDING PAGE
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{city} 2026 Stay Matrix | Vulture Global</title>
    <meta name="description" content="Direct AI access to {city} hotel inventory and secret 2026 World Cup rates.">
    <style>
        body {{ background: #010409; color: #8b949e; font-family: sans-serif; padding: 50px; line-height: 1.6; }}
        h2 {{ color: #ffd700; }}
        .cta {{ display: inline-block; background: #ffd700; color: #000; padding: 15px 25px; text-decoration: none; font-weight: bold; border-radius: 5px; }}
    </style>
</head>
<body>
    {content}
    <br><br>
    <a href="{BASE_URL}?city={slug}" class="cta">INITIALIZE {city.upper()} SNATCH</a>
    <hr style="border: 0; border-top: 1px solid #30363d; margin: 40px 0;">
    <p style="font-size: 0.7rem;">&copy; 2026 Vulture Global Domination Protocol | Node: {slug}</p>
</body>
</html>"""

        with open(f"{node_path}/index.html", "w") as f:
            f.write(html)

    print("✅ ARTICLES INJECTED INTO NODES.")

if __name__ == "__main__":
    generate_articles()
