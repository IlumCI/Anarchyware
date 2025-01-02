var map = L.map('map').setView([48.8566, 2.3522], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

fetch('/api/targets')
    .then(response => response.json())
    .then(data => {
        data.forEach(target => {
            L.marker([target.lat, target.lon])
                .addTo(map)
                .bindPopup(`<b>${target.name}</b><br>${target.industry}`);
        });
    });
