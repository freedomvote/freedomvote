jQuery(function ($){
  'use strict'

  const sizeXs = 767

  function initChart(data) {
    $('.statistic').each(function(){
      var id = this.id.replace('statistic-', '')

      $.getJSON($(this).data('url'), function(data){
        $('#statistic-' + id).highcharts({
          chart: {
            type: 'bar',
            backgroundColor: 'transparent',
            height: data.values.length * 20 * (deviceWidth <= sizeXs ? 2.5 : 1)
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
  }

  var deviceWidth = $(window).width()

  initChart()

  $(window).resize(function() {
    var newDeviceWidth = $(window).width()

    if ((deviceWidth <= sizeXs && newDeviceWidth > sizeXs) || (deviceWidth > sizeXs && newDeviceWidth <= sizeXs)) {
      $('.statistic').each(function() {
        var chart = $(this).highcharts()
        var height = chart.series[0].data.length * 20 * (newDeviceWidth <= sizeXs ? 2.5 : 1)
        var width = $(this).width
        chart.setSize(width, height, false)
      })
    }

    deviceWidth = newDeviceWidth
  })

});
