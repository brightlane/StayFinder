const fs = require('fs');

// 1. Configuration
const BASE_URL = 'https://brightlane.github.io/StayFinder/';
const KEYWORDS_FILE = 'keywords.txt'; // Your list of 10,000 slugs
const SITEMAP_FILE = 'sitemap.xml';
const DATE = new Date().toISOString().split('T')[0];

// 2. Sitemap Header
let xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>${BASE_URL}</loc>
    <lastmod>${DATE}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>`;

// 3. Inject Keywords
try {
    const keywords = fs.readFileSync(KEYWORDS_FILE, 'utf8').split('\n');
    
    keywords.forEach(line => {
        const slug = line.trim().replace(/\s+/g, '-').toLowerCase();
        if (slug) {
            xml += `
  <url>
    <loc>${BASE_URL}${slug}</loc>
    <lastmod>${DATE}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>`;
        }
    });

    // 4. Close and Save
    xml += '\n</urlset>';
    fs.writeFileSync(SITEMAP_FILE, xml);
    console.log(`✅ Success: ${keywords.length} URLs injected into ${SITEMAP_FILE}`);

} catch (err) {
    console.error("❌ Error reading keywords.txt:", err);
}
