// Total Revenue by Department
const departmentCtx = document.getElementById('departmentChart').getContext('2d');
const departmentChart = new Chart(departmentCtx, {
    type: 'bar',
    data: {
        labels: JSON.parse(document.getElementById('departmentLabels').textContent),
        datasets: [{
            label: 'Recaudación Total',
            data: JSON.parse(document.getElementById('departmentData').textContent),
            backgroundColor: 'rgba(75, 192, 192, 0.6)',
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: true
            },
            tooltip: {
                callbacks: {
                    label: function (tooltipItem) {
                        return 'Q ' + tooltipItem.raw.toLocaleString('es-GT');
                    }
                }
            },
            title: {
                display: true,
                text: 'Recaudación Total por Departamento'
            },
            zoom: {
                pan: {
                    enabled: true,
                    mode: 'x',
                },
                zoom: {
                    wheel: {
                        enabled: true,
                    },
                    pinch: {
                        enabled: true
                    },
                    mode: 'x',
                }
            }
        },
        scales: {
            y: {
                ticks: {
                    callback: function (value) {
                        return 'Q ' + value.toLocaleString('es-GT');
                    }
                },
                title: {
                    display: true,
                    text: 'Recaudación Total (Q)'
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Departamento'
                }
            }
        }
    }
});

// Revenue Distribution by Tax
const taxCtx = document.getElementById('taxChart').getContext('2d');
const taxChart = new Chart(taxCtx, {
    type: 'pie',
    data: {
        labels: ['IVA Importación', 'Derecho Arancelario a la Importación (DAI)', 'Impuesto Sobre la Renta (ISR)', 'Impuesto de Solidaridad (ISO)', 'IVA Doméstico'],
        datasets: [{
            data: JSON.parse(document.getElementById('taxData').textContent),
            backgroundColor: [
                'rgba(255, 99, 132, 0.6)',
                'rgba(54, 162, 235, 0.6)',
                'rgba(255, 206, 86, 0.6)',
                'rgba(75, 192, 192, 0.6)',
                'rgba(153, 102, 255, 0.6)'
            ]
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: true
            },
            tooltip: {
                callbacks: {
                    label: function (tooltipItem) {
                        const value = tooltipItem.raw;
                        return 'Q ' + value.toLocaleString('es-GT');
                    }
                }
            },
            title: {
                display: true,
                text: 'Distribución de la Recaudación por Impuesto'
            }
        }
    }
});

// Revenue Trends by Year
const yearlyCtx = document.getElementById('yearlyChart').getContext('2d');
const yearlyChart = new Chart(yearlyCtx, {
    type: 'line',
    data: {
        labels: JSON.parse(document.getElementById('yearlyLabels').textContent),
        datasets: [{
            label: 'Recaudación Total',
            data: JSON.parse(document.getElementById('yearlyData').textContent),
            borderColor: 'rgba(75, 192, 192, 1)',
            fill: false,
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: true
            },
            tooltip: {
                callbacks: {
                    label: function (tooltipItem) {
                        return 'Q ' + tooltipItem.raw.toLocaleString('es-GT');
                    }
                }
            },
            title: {
                display: true,
                text: 'Tendencias de Recaudación por Año'
            }
        },
        scales: {
            y: {
                ticks: {
                    callback: function (value) {
                        return 'Q ' + value.toLocaleString('es-GT');
                    }
                },
                title: {
                    display: true,
                    text: 'Recaudación Total (Q)'
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Año'
                }
            }
        }
    }
});
