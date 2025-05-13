fetch('/getPriorities')
    .then(response => response.json())
    .then(data => {
        const div = document.getElementById('priorities');
        div.innerHTML = '<h2>Priorities:</h2><ul>' +
            data.map(p => `<li>${p.Prioritaet}</li>`).join('') + '</ul>';
    })
    .catch(err => console.error('Fetch error:', err));
