jQuery(function ($){
  "use strict";

  $('.statistic').each(function(){
    var id = $(this).attr('id').replace('statistic-', '')

    $.getJSON('/statistic/' + id + '/')
    .success(function(data){
      $('#statistic-' + id).highcharts({
        chart: {
          type: 'column',
          backgroundColor: 'transparent'
        },
        title: {
          text: ' '
        },
        subtitle: {
          text: ' '
        },
        xAxis: {
          categories: data.categories,
          labels: {
            rotation: 320,
          }
        },
        credits: {
          enabled: false
        },
        yAxis: {
          min: 0,
          max: 10,
          title: ' ',
          minorTickInterval: 1,
          labels: {
            enabled: false
          }
        },
        tooltip: false,
        plotOptions: {
          column: {
            pointPadding: 0.2,
            borderWidth: 0
          }
        },
        legend: {
          enabled: false
        },
        series: [{
          colorByPoint: true,
          data: data.values
        }]
      });
    })
  })

});
