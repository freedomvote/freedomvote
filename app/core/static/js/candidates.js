jQuery(function($) {
  'use strict'

  $('.add-popover').each(function() {
    $(this).popover({container:'body', html:true})
  })

  $('.statistic').each(function(){
    var id = this.id.replace('statistic-', '')

    $.getJSON($(this).data('url'), function(data) {
      var margin = data.summary.titles.length > 1 ? 0 : 30
      $('#statistic-' + id).highcharts({
        chart: {
          type: 'bar',
          marginTop: margin / 2,
          marginBottom: margin / 2,
          backgroundColor: 'transparent',
          height: 60
        },
        title: null,
        xAxis: {
          categories: data.summary.titles,
          title: null
        },
        yAxis: {
          min: 0,
          max: 10,
          minorTickInterval: 1,
          title: null,
          labels: {
            enabled: false
          }
        },
        credits: {
          enabled: false
        },
        legend: {
          enabled: false
        },
        tooltip: false,
        plotOptions: {
          bar: {
            stacking: 'normal',
            pointWidth: 15
          },
          series: {
            point: {
              events: {
                click: function(e) {
                  var rect   = $(this.graphic.element)
                  var charts = rect.closest('.charts')
                  var detail = charts.children('.detail')

                  var effect = 'drop'

                  $('.detail').not(detail).hide(effect)

                  detail.toggle(effect, function(e) {
                    window.dispatchEvent(new Event('resize'));
                  })
                }
              }
            }
          }
        },
        series: [{
          name: '',
          data: data.summary.values.negative,
          color: '#990000'
        }, {
          name: '',
          data: data.summary.values.positive,
          color: '#009900'
        }]
      })

      $('#detail-' + id).highcharts({
        chart: {
          type: 'bar',
          backgroundColor: 'transparent',
          height: data.detail.categories.length * 25 + 20
        },
        title: {
          text: ' '
        },
        subtitle: {
          text: ' '
        },
        xAxis: {
          categories: data.detail.categories
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
          },
          bar: {
            pointWidth: 15
          }
        },
        legend: {
          enabled: false
        },
        series: [{
          colorByPoint: true,
          data: data.detail.values
        }]
      })
    })
  })
});
