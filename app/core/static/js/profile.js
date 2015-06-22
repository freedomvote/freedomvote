jQuery(function ($){
  'use strict'

  const sliderOffset = 7
  const colors = [
    {
      fill : 'rgba(124,181,236,0.75)',
      stroke : '#7cb5ec'
    },
    {
      fill : 'rgba(67,67,72,0.75)',
      stroke : '#434348'
    }
  ]

  $('.slider-readonly').each(function() {
    createReadonlySlider($(this))
  })

  function createReadonlySlider(slider) {
    slider.empty()

    var svg = '<svg viewBox="0 0 300 20" preserveAspectRatio="xMinYMin meet">' +
              '<rect x="'+sliderOffset+'" y="5" rx="3" ry="3" height="10" width="'+(300-sliderOffset*2)+'"'+
              'style="fill:rgb(200,200,200);stroke-width:1;stroke:rgb(150,150,150)" />'

    var values = slider.data('slider-value')
    var titles = slider.data('slider-title')
    var texts  = slider.data('slider-text')

    for (var i = 0; i < values.length; i++) {
      var ci     = i > (colors.length - 1) ? 0 : i
      var color  = colors[ci]
      var posX   = sliderOffset + ((300 - sliderOffset * 2) / 10 * values[i])
      var posY   = i % 2 == 0 ? -10 : 10

      svg += '<path class="add-popover" data-title="'+titles[i]+'" data-text="'+texts[i]+'"'+
             'd="M '+posX+' 10 l-7 '+posY+' l14 0 l-7 '+(-1*posY)+'" fill="'+color.fill+'" stroke-width="1" stroke="'+color.stroke+'" />'
    }

    slider.append(svg + '</svg>')

    slider.find('.add-popover').each(function(){
      $(this).popover({
        title: $(this).data('title'),
        content: $(this).data('text'),
        container: 'body',
        trigger: 'hover',
        placement: 'top'
      })
    })
  }

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
