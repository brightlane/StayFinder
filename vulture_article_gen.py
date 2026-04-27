import os

# CONFIG
KEYWORDS_FILE = 'keywords.txt'
BASE_URL = 'https://brightlane.github.io/SkyScanner/'

TEMPLATES = [
    """<h2>2026 Inventory Report: {city}</h2>
    <p>The global housing matrix for 2026 is tightening. In {city}, we are seeing a massive surge in direct-to-inventory requests.</p>
    <p>Accessing {city} via the Vulture Protocol ensures you bypass the standard retail markups typically added by travel agencies.</p>""",
    
    """<h2>Sniper Alert: {city} Stadium District</h2>
    <p>Our nodes have detected a price drop in {city}. While retail platforms show 'Sold Out,' the direct inventory layer still shows availability.</p>
    <p>By using the Vulture Matrix, travelers access mobile-only Genius Tier 3 rates for {city}.</p>"""
]

def generate_articles():
    if not os.path.exists(KEYWORDS_FILE): return
    with open(KEYWORDS_FILE, 'r') as f:
        cities = [line.strip() for line in f if line.strip()]

    for i, city in enumerate(cities):
        slug = city.lower().replace(" ", "-")
        node_path = f"nodes/{slug}"
        os.makedirs(node_path, exist_ok=True)
        content = TEMPLATES[i % len(TEMPLATES)].format(city=city)

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{city} 2026 Stay Matrix | Vulture Global</title>
    <style>
        body {{ background: #010409; color: #8b949e; font-family: sans-serif; padding: 50px; line-height: 1.6; text-align: center; }}
        h2 {{ color: #ffd700; text-transform: uppercase; }}
        .cta {{ display: inline-block; background: #ffd700; color: #000; padding: 15px 25px; text-decoration: none; font-weight: bold; border-radius: 5px; margin-top: 20px; }}
    </style>
</head>
<body>
    {content}
    <a href="{BASE_URL}?city={slug}" class="cta">INITIALIZE {city.upper()} SNATCH</a>
</body>
</html>"""
        with open(f"{node_path}/index.html", "w") as f:
            f.write(html)

if __name__ == "__main__":
    generate_articles()
