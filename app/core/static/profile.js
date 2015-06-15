jQuery(function ($){
  'use strict'

  const sliderOffset = 7
  const colors = [
    {
      fill : 'rgb(65,165,63)',
      stroke : 'rgb(54,142,78)'
    },
    {
      fill : 'rgb(91,205,253)',
      stroke : 'rgb(83,148,230)'
    }
  ]

  $('.slider-readonly').each(function() {
    createReadonlySlider($(this))
  })

  function createReadonlySlider(slider) {
    var barWidth = slider.width() - (sliderOffset * 2)
    var svg = '<svg width="'+slider.width()+'" height="30">' +
              '<rect x="'+sliderOffset+'" y="10" rx="3" ry="3" height="10" width="'+barWidth+'"'+
              'style="fill:rgb(200,200,200);stroke-width:1;stroke:rgb(150,150,150)" />'

    var values = slider.data('slider-value')
    var titles = slider.data('slider-title')
    var texts  = slider.data('slider-text')

    for (var i = 0; i < values.length; i++) {
      var value  = values[i]
      var title  = titles[i]
      var text   = texts[i]
      var ci     = i > (colors.length - 1) ? 0 : i
      var color  = colors[ci]
      var posX   = sliderOffset + barWidth / 10 * value
      var posY   = i % 2 == 0 ? 0 : 30

      svg += '<polygon class="add-popover" data-title="'+title+'" data-text="'+text+'"'+
             'points="'+posX+',15 '+(posX-sliderOffset)+','+posY+' '+(posX+sliderOffset)+','+posY+'" style="fill:'+color.fill+';stroke-width:1;stroke:'+color.stroke+'" />'
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

  $.getJSON(Urls.profile_info(item.data('politician-id')) + '?compare', function(data){
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
