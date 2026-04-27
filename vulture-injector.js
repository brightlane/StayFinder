const fs = require('fs');

/**
 * VULTURE PROTOCOL: MILLION-NODE INJECTOR (Node.js)
 * Automatically splits 100,000+ keywords into Google-compliant chunks.
 */

// 1. CONFIGURATION
const BASE_URL = 'https://brightlane.github.io/SkyScanner/'; // Updated to your active repo
const KEYWORDS_FILE = 'keywords.txt';
const MAX_URLS_PER_FILE = 45000; // Stay safe under Google's 50k limit
const TODAY = new Date().toISOString().split('T')[0];

try {
    if (!fs.existsSync(KEYWORDS_FILE)) {
        console.log(`⚠️  Vulture Warning: ${KEYWORDS_FILE} missing. Generating seed file...`);
        fs.writeFileSync(KEYWORDS_FILE, 'dallas-stadium\n75201-hotels\ntokyo-resorts');
    }

    const data = fs.readFileSync(KEYWORDS_FILE, 'utf8');
    const keywords = data.split('\n').filter(line => line.trim() !== '');
    const totalNodes = keywords.length;
    const sitemapsNeeded = Math.ceil(totalNodes / MAX_URLS_PER_FILE);

    let sitemapIndexXml = `<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`;

    for (let i = 0; i < sitemapsNeeded; i++) {
        const batch = keywords.slice(i * MAX_URLS_PER_FILE, (i + 1) * MAX_URLS_PER_FILE);
        const fileName = `sitemap-${i + 1}.xml`;
        
        // Build Individual Sitemap
        let xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>${BASE_URL}</loc>
        <lastmod>${TODAY}</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>`;

        batch.forEach(keyword => {
            // Clean the keyword and format as a URL parameter for index.html
            const slug = keyword.trim()
                .toLowerCase()
                .replace(/[^a-z0-9]/g, '-')
                .replace(/-+/g, '-');

            xml += `
    <url>
        <loc>${BASE_URL}?city=${slug}</loc>
        <lastmod>${TODAY}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>`;
        });

        xml += '\n</urlset>';
        fs.writeFileSync(fileName, xml);
        
        // Add this file to the Master Index
        sitemapIndexXml += `  <sitemap>\n    <loc>${BASE_URL}${fileName}</loc>\n    <lastmod>${TODAY}</lastmod>\n  </sitemap>\n`;
        console.log(`📡 Generated ${fileName} (${batch.length} nodes)`);
    }

    // Save the Master Index
    sitemapIndexXml += '</sitemapindex>';
    fs.writeFileSync('sitemap.xml', sitemapIndexXml);
    console.log(`✅ SUCCESS: ${totalNodes} nodes across ${sitemapsNeeded} sitemaps linked in sitemap.xml`);

} catch (err) {
    console.error("❌ Vulture Protocol Error:", err);
}
