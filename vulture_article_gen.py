import os

KEYWORDS_FILE = 'keywords.txt'
BASE_URL = 'https://brightlane.github.io/SkyScanner/'

# NETWORK NODES for Cross-Linking
SISTER_SITES = [
    "https://brightlane.github.io/booking.com/",
    "https://brightlane.github.io/booking/",
    "https://brightlane.github.io/BookingMaster/"
]

TEMPLATES = [
    """<h2>2026 Inventory Report: {city}</h2>
    <p>The global housing matrix for 2026 is tightening. In {city}, we are seeing surge in direct-to-inventory requests.</p>
    <p>Cross-verify this node at our <a href="{site}" style="color:#ffd700;">Secondary Matrix</a> for rate parity.</p>""",
    
    """<h2>Sniper Alert: {city} Stadium District</h2>
    <p>Our AI detected a price drop in {city}. While retail shows 'Sold Out,' the direct layer is open.</p>
    <p>Access the <a href="{site}" style="color:#ffd700;">Global Inventory Node</a> to bypass retail markups.</p>"""
]

def generate_articles():
    if not os.path.exists(KEYWORDS_FILE): return
    with open(KEYWORDS_FILE, 'r') as f:
        cities = [line.strip() for line in f if line.strip()]

    for i, city in enumerate(cities):
        slug = city.lower().replace(" ", "-")
        node_path = f"nodes/{slug}"
        os.makedirs(node_path, exist_ok=True)
        
        # Pick a sister site to backlink
        sister_site = SISTER_SITES[i % len(SISTER_SITES)]
        content = TEMPLATES[i % len(TEMPLATES)].format(city=city, site=sister_site)

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{city} 2026 Stay Matrix</title>
    <style>
        body {{ background: #010409; color: #8b949e; font-family: sans-serif; padding: 50px; text-align: center; }}
        h2 {{ color: #ffd700; }}
        .cta {{ display: inline-block; background: #ffd700; color: #000; padding: 15px 25px; text-decoration: none; font-weight: bold; border-radius: 5px; }}
    </style>
</head>
<body>
    {content}
    <br><br>
    <a href="{BASE_URL}?city={slug}" class="cta">INITIALIZE {city.upper()} SNATCH</a>
</body>
</html>"""
        with open(f"{node_path}/index.html", "w") as f:
            f.write(html)

if __name__ == "__main__":
    generate_articles()
