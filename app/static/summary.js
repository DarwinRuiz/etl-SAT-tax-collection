document.addEventListener('DOMContentLoaded', function () {
    const filterForm = document.getElementById('filterForm');
    const summaryTableBody = document.getElementById('summaryTableBody');


    // Manage the filter form
    filterForm.addEventListener('submit', function (e) {
        e.preventDefault();

        // Get filter values
        const activity = document.getElementById('activity').value;
        const department = document.getElementById('department').value;
        const year = document.getElementById('year').value;

        // Create the URL with filter parameters
        const url = new URL('/api/summary', window.location.origin);
        if (activity) url.searchParams.append('activity', activity);
        if (department) url.searchParams.append('department', department);
        if (year) url.searchParams.append('year', year);

        // Fetch to get the filtered summary
        fetch(url)
            .then(response => response.json())
            .then(data => {
                summaryTableBody.innerHTML = '';

                data.forEach(row => {
                    const tr = document.createElement('tr');
                    tr.innerHTML = `
                        <td>${row.activity_name}</td>
                        <td>${row.department}</td>
                        <td>${row.year}</td>
                        <td>Q ${row.total_revenue.toLocaleString('es-GT')}</td>
                    `;
                    summaryTableBody.appendChild(tr);
                });
            });
    });

});
