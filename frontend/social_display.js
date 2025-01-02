fetch('/api/employees')
    .then(response => response.json())
    .then(data => {
        data.forEach(employee => {
            let marker = L.marker([target.lat, target.lon])
                .addTo(map)
                .bindPopup(`
                    <b>${employee.name}</b><br>
                    LinkedIn: <a href="${employee.profile_url}" target="_blank">Profile</a><br>
                    Company: ${employee.company}
                `);
        });
    });

fetch('/api/breaches')
    .then(response => response.json())
    .then(data => {
        data.forEach(breach => {
            let popupContent = `
                <b>Email Breach Detected</b><br>
                Email: ${breach.email}<br>
                Breaches: ${breach.breach_name}<br>
            `;
            L.popup().setLatLng([target.lat, target.lon]).setContent(popupContent).openOn(map);
        });
    });
