jQuery(function ($){
  'use strict'

  var item = $('#chart')

  $.getJSON(item.data('url'), function(data){
    item.highcharts({
      chart: {
        polar: true,
        type: 'area',
        backgroundColor: 'transparent',
        spacing: [ 10, 90, 10, 90 ]
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
      },{
        pointPlacement: 'on',
        data: data.values.citizen,
        visible: $('#show_citizen').prop('checked'),
      }]
    });
  })

  $('#show_citizen').on('change', function(){
    if ($(this).prop('checked')) {
      item.highcharts().series[1].show()
    }
    else {
      item.highcharts().series[1].hide()
    }
  })
});
