def generate_vulture_sitemap(nodes):
    base_url = "https://brightlane.github.io/SkyScanner/"
    
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for node in nodes:
        clean_node = node.lower().replace(" ", "-")
        xml += f'  <url>\n    <loc>{base_url}?city={clean_node}</loc>\n    <changefreq>daily</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
    
    xml += '</urlset>'
    
    with open('sitemap.xml', 'w') as f:
        f.write(xml)
    print("🛰️ Sitemap generated for Google Search Console.")

# Run this with the same list as the dictionary
generate_vulture_sitemap(world_cup_nodes + global_cities)
