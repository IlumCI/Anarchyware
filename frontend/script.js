var map = L.map('map').setView([48.8566, 2.3522], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

function getMarkerColor(score) {
    if (score < 40) return 'green';
    if (score < 70) return 'orange';
    return 'red';
}

fetch('/api/targets')
    .then(response => response.json())
    .then(data => {
        data.forEach(target => {
            let marker = L.marker([target.lat, target.lon])
                .addTo(map)
                .bindPopup(`
                    <b>${target.name}</b><br>
                    Industry: ${target.industry}<br>
                    Score: ${target.score}/100<br>
                    SSL Validity: ${target.ssl_valid_days} days<br>
                    Domain Age: ${target.domain_age} years
                `);
        });
    });
