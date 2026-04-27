// VULTURE CROSS-LINK INJECTOR
const globalNodes = [
    "London", "Paris", "Tokyo", "New York", "Dubai", "Miami", "Dallas", "Bali", "Rome", "Sydney"
];

function injectVultureLinks() {
    const footer = document.createElement('footer');
    footer.style.cssText = "padding: 50px; background: #000; border-top: 1px solid #333; text-align: center; color: #666; font-size: 0.7rem;";
    
    let linkHTML = '<p style="margin-bottom: 20px; color: #ffd700; font-weight: 900;">GLOBAL NODE NETWORK</p>';
    
    globalNodes.forEach(city => {
        linkHTML += `<a href="index.html?city=${city.toLowerCase()}" style="color: #888; text-decoration: none; margin: 0 10px;">${city} Matrix</a> | `;
    });

    footer.innerHTML = linkHTML + "<p style='margin-top:20px;'>&copy; 2026 VULTURE GLOBAL DOMINATION PROTOCOL</p>";
    document.body.appendChild(footer);
}

document.addEventListener('DOMContentLoaded', injectVultureLinks);
