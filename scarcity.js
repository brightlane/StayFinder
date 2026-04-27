// VULTURE SCARCITY & TRUST ENGINE
const hunters = ["Guest1204", "User_882", "TravelSniper", "Matrix_Hunter", "Alpha_Voyager"];
const actions = ["just secured 40% off", "sniped a Genius Tier 3 rate", "extracted a Mobile-Only deal", "unlocked Secret Inventory"];

function showNotification() {
    const notification = document.createElement('div');
    const randomHunter = hunters[Math.floor(Math.random() * hunters.length)];
    const randomAction = actions[Math.floor(Math.random() * actions.length)];
    const params = new URLSearchParams(window.location.search);
    const city = params.get('city') || "Global Inventory";

    notification.style.cssText = `
        position: fixed; bottom: 20px; left: 20px; 
        background: rgba(0, 255, 65, 0.1); border: 1px solid #00ff41; 
        color: #00ff41; padding: 15px; border-radius: 10px; 
        font-family: monospace; font-size: 0.7rem; z-index: 10000;
        box-shadow: 0 0 20px rgba(0, 255, 65, 0.2);
        backdrop-filter: blur(5px); transition: opacity 0.5s;
    `;

    notification.innerHTML = `📡 <strong>LIVE FEED:</strong> ${randomHunter} ${randomAction} in <strong>${city.toUpperCase()}</strong>.`;
    
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.opacity = '0';
        setTimeout(() => notification.remove(), 500);
    }, 4000);
}

// Trigger every 8-15 seconds
setInterval(showNotification, Math.floor(Math.random() * 7000) + 8000);
