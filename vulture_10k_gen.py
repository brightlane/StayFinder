import os
import json
import re

# --- VULTURE CONFIGURATION ---
BASE_URL = "https://brightlane.github.io/SkyScanner/"
KEYWORDS_FILE = "keywords.txt" # Your 10,000 to 1,000,000 city/zip list
AFFILIATE_ID = "8132800" # Your Skyscanner/Booking ID
VERSION = "2026.4.27"

def clean_slug(text):
    return re.sub(r'[^a-z0-9]', '-', text.lower()).strip('-')

def generate_vulture_nodes():
    # 1. Load the Target Keywords
    if not os.path.exists(KEYWORDS_FILE):
        print(f"❌ ERROR: {KEYWORDS_FILE} not found. Sniper aborted.")
        return

    with open(KEYWORDS_FILE, 'r', encoding='utf-8') as f:
        nodes = [line.strip() for line in f if line.strip()]

    print(f"🦅 VULTURE 10K PROTOCOL STARTING... TARGETING {len(nodes)} NODES.")

    # 2. Create the Node Directory Structure
    # Using 'nodes' folder to keep the root clean
    if not os.path.exists('nodes'):
        os.makedirs('nodes')

    manifest_data = []

    for node in nodes:
        slug = clean_slug(node)
        node_dir = f"nodes/{slug}"
        
        if not os.path.exists(node_dir):
            os.makedirs(node_dir)

        # 3. Create the Physical SEO Redirect File
        # This forces Google to index the keyword while redirecting to the Command Center
        index_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>{node.upper()} | Stay Matrix Sniper</title>
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{BASE_URL}?city={slug}">
    <script>window.location.replace("../../index.html?city={slug.replace('-', '%20')}");</script>
</head>
<body>Redirecting to Node {slug}...</body>
</html>"""

        with open(f"{node_dir}/index.html", "w", encoding="utf-8") as f:
            f.write(index_content)

        # 4. Prepare Data for the Global Manifest
        manifest_data.append(node)

    # 5. Output the Global Nodes JSON (The Fuel for the UI)
    # We split by first letter for the high-speed autocomplete engine
    tiered_manifest = {}
    for item in manifest_data:
        char = item[0].upper()
        if char not in tiered_manifest:
            tiered_manifest[char] = []
        tiered_manifest[char].append(item)

    with open('global_nodes.json', 'w', encoding='utf-8') as f:
        json.dump(tiered_manifest, f)

    print(f"✅ PROTOCOL COMPLETE. {len(nodes)} physical nodes built.")
    print(f"📡 'global_nodes.json' updated for Matrix UI.")

if __name__ == "__main__":
    generate_vulture_nodes()
