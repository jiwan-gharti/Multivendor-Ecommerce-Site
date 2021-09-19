console.log('Chart js')

var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [`5 star`, '4 star', '3 star', '2 star', '1 star'],
        datasets: [{
            data: [12, 19, 3, 5, 2],
            backgroundColor: ['lightgray'],
            borderRadius : 10,
            barThickness: 12,
        }],
    },
    options: {
        indexAxis: 'y',
        responsive : true,
        layout : {
            padding: 30,
        },
        plugins: {
            tooltip: {
                enabled: false,
            },
            legend: {
                display : false,
            },
        },
        scales: {
            x: {
                display : false,
            },
            y:{
                ticks: {
                    color: 'green',
                    font: {
                        size: 20,
                        family: 'Aeria',
                    }
                },
                grid : {
                    display : false,
                },
            }
        },
      },
    
});