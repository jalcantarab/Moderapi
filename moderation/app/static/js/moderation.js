
document.querySelector('form').addEventListener('submit', function (event) {
    event.preventDefault();
    const contentInput = document.getElementById('content-input');
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const formData = new FormData();
    formData.append('content', contentInput.value);
    formData.append('csrfmiddlewaretoken', csrfToken);
    fetch('/moderation-api/', {
        method: 'POST',
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                const resultsContainer = document.getElementById('resultsContainer');
                const resultsList = document.getElementById('resultsList');
                var categories = '';
                resultsContainer.style.display = 'block';
                resultsList.innerHTML = '';

                for (const [category, score] of Object.entries(data.scores)) {
                    const score100 = (score*100).toFixed(2); 
                    const categoryHTML = `
                    <li class="list-group-item d-flex justify-content-between align-items-center" id="result-${category}">
                        ${category}
                        <span class="badge bg-primary" id="score-${category}">${score100}</span>
                    </li>
                    `;
                    categories += categoryHTML;
                }

                resultsList.innerHTML = categories;
            } else {
                alert(`Error: ${data.error}`);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
});