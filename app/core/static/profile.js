jQuery(function ($){
  "use strict";

  $('.slider-readonly').each(function() {
    var value = $(this).data('value')
      $(this).slider({
        max: 10,
        min: 0,
        value: value,
        step: 2,
        disabled: true
      })
  })

  var item = $('#chart')

  $.getJSON(Urls.profile_info(item.data('politician-id')) + '?compare', function(data){
    item.highcharts({
      chart: {
        polar: true,
        type: 'area',
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
