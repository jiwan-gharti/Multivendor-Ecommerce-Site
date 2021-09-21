
var ctx = document.getElementById("merchant_dashboard_chart").getContext("2d");

var merchant_line_plot = new Chart(ctx, {
    type:'line',
    data:{
        labels: ['a','b','c','d','e'],
        datasets : [{
            label: 'My First Dataset',
            data: [65, 59, 80, 81, 56, 55, 40],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    }
});

var ctx1 = document.getElementById("merchant_bar_plot").getContext("2d")

var merchant_bar_plot = new Chart(ctx1,{
    type : "bar",
    data : {
        labels: ['First','Second','Third','Fourth','Fifth'],
        datasets: [{
          label: 'My First Dataset',
          data: [65, 59, 80, 81, 56],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(255, 205, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(54, 162, 235, 0.2)',
          ],borderColor: [
            'rgb(255, 99, 132)',
            'rgb(255, 159, 64)',
            'rgb(255, 205, 86)',
            'rgb(75, 192, 192)',
            'rgb(54, 162, 235)',
          ],
          borderWidth: 1
        }]
    }
});