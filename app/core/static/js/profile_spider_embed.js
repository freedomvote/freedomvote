jQuery(function ($){
  'use strict'

  var item = $('#chart')

  $.getJSON(item.data('url'), function(data){
    item.highcharts({
      chart: {
        polar: true,
        type: 'area',
        height: 280,
        width: 400,
        backgroundColor: 'transparent',
      },
      title: {
        text: null
      },
      subtitle: {
        text: null
      },
      xAxis: {
        categories: data.categories,
        tickmarkPlacement: 'on',
        lineWidth: 0
      },
      credits: {
        enabled: false
      },
      yAxis: {
        min: 0,
        max: 10,
        title: ' ',
        gridLineInterpolation: 'polygon',
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
        pointPlacement: 'on',
        data: data.values.politician
      }]
    });
  })
})
