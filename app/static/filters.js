document.addEventListener('DOMContentLoaded', function () {
    const activitySelect = document.getElementById('activity');
    const departmentSelect = document.getElementById('department');
    const yearSelect = document.getElementById('year');

    // Load filter options from the backend
    fetch('/api/summary/options')
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error al cargar opciones: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            populateSelectActivities(activitySelect, data.activities);
            populateSelect(departmentSelect, data.departments);
            populateSelect(yearSelect, data.years);
        })
        .catch(error => {
            console.error('Error al cargar las opciones de los filtros:', error);
        });

    // Function to populate the selects
    function populateSelectActivities(selectElement, options) {
        options.forEach(option => {
            const opt = document.createElement('option');
            opt.value = option.activity_id;
            opt.textContent = option.activity_name;
            selectElement.appendChild(opt);
        });
    }

    function populateSelect(selectElement, options) {
        options.forEach(option => {
            const opt = document.createElement('option');
            opt.value = option;
            opt.textContent = option;
            selectElement.appendChild(opt);
        });
    }
});
