const fs = require('fs');

/**
 * VULTURE 10K PROTOCOL: AUTOMATED SITEMAP INJECTOR
 * This script generates a massive, Google-ready sitemap from your keyword list.
 */

// 1. CONFIGURATION
const BASE_URL = 'https://brightlane.github.io/StayFinder/';
const KEYWORDS_FILE = 'keywords.txt'; // Create this file with one keyword/zip per line
const SITEMAP_FILE = 'sitemap.xml';
const TODAY = new Date().toISOString().split('T')[0];

// 2. SITEMAP HEADER
let xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>${BASE_URL}</loc>
        <lastmod>${TODAY}</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>`;

// 3. KEYWORD PROCESSING LOGIC
try {
    if (!fs.existsSync(KEYWORDS_FILE)) {
        console.log(`⚠️  Vulture Warning: ${KEYWORDS_FILE} not found. Creating empty file...`);
        fs.writeFileSync(KEYWORDS_FILE, 'miami-beach-penthouses\n77001-hotels\nmarriott-rome-deals');
    }

    const data = fs.readFileSync(KEYWORDS_FILE, 'utf8');
    const keywords = data.split('\n').filter(line => line.trim() !== '');

    keywords.forEach(keyword => {
        // Clean the keyword to create a valid SEO slug
        const slug = keyword.trim()
            .toLowerCase()
            .replace(/[^a-z0-9]/g, '-') // Replace non-alphanumeric with hyphens
            .replace(/-+/g, '-');      // Remove double hyphens

        xml += `
    <url>
        <loc>${BASE_URL}${slug}</loc>
        <lastmod>${TODAY}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>`;
    });

    // 4. CLOSE AND SAVE
    xml += '\n</urlset>';
    fs.writeFileSync(SITEMAP_FILE, xml);
    console.log(`✅ Vulture Protocol Success: ${keywords.length} URLs injected into ${SITEMAP_FILE}`);

} catch (err) {
    console.error("❌ Vulture Protocol Error:", err);
}
