jQuery(function ($){
  "use strict";

  $('.statistic').each(function(){
    var id = this.id.replace('statistic-', '')

    $.getJSON($(this).data('url'), function(data){
      $('#statistic-' + id).highcharts({
        chart: {
          type: 'bar',
          backgroundColor: 'transparent',
          height: data.values.length * 25
        },
        title: {
          text: ' '
        },
        subtitle: {
          text: ' '
        },
        xAxis: {
          categories: data.categories,
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
