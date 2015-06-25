jQuery(function() {
  'use strict'

  var mousePos = { x: 0, y: 0 }

  $('.add-popover').each(function() {
    $(this).popover({container:'body', html:true})
  })

  $(window).on('mousemove', function(e) {
    mousePos = { x: e.pageX, y: e.pageY }
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
                mouseOver: function(e) {
                  var rect = $(this.graphic.element)
                  var detail = rect.parents('.charts').children('.detail')
                  detail.css({
                    top: rect.offset().top + rect.height() + 30,
                    left: mousePos.x - detail.width() / 2 + 'px'
                  }).fadeIn()
                },
                mouseOut: function(e) {
                  $(this.graphic.element).parents('.charts').children('.detail').fadeOut()
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
          categories: data.detail.categories,
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
