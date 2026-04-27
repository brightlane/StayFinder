import os

# CONFIGURATION
BASE_URL = "https://brightlane.github.io/SkyScanner/"
CITIES = ["london", "paris", "tokyo", "dallas", "dubai", "new-york"] # Extend this to 1M
TYPES = ["hotel", "villa", "resort", "bnb"]

def generate_vulture_nodes():
    if not os.path.exists('nodes'):
        os.makedirs('nodes')

    for city in CITIES:
        for stay_type in TYPES:
            filename = f"nodes/{city}-{stay_type}.html"
            with open(filename, "w") as f:
                # INJECTING YOUR GLOBAL SEO ARCHITECTURE
                f.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Best {stay_type}s in {city.title()} | Vulture 2026 Secret Rates</title>
    <meta name="description" content="Sniping direct inventory for {stay_type}s in {city.title()}. Mobile-only pricing active.">
    <link rel="canonical" href="{BASE_URL}{filename}">
    <script>window.location.href="../index.html?city={city}&type={stay_type}";</script>
</head>
<body>Redirecting to Vulture Matrix...</body>
</html>
                """)
    print(f"Generated {len(CITIES) * len(TYPES)} Vulture Nodes.")

if __name__ == "__main__":
    generate_vulture_nodes()
