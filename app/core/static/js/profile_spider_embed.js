jQuery(function ($){
  'use strict'

  var item = $('#chart'),
      sourceUrl = "//" + item.data('source');

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
        enabled: true
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
  // Credits to Hampus Nilsson (https://hjnilsson.com/2016/02/26/highcharts-open-credits-in-new-tab/)
  Highcharts.wrap(Highcharts.Chart.prototype, 'showCredits', function (next, credits) {
    next.call(this, credits);

    if (credits.enabled) {
      this.credits.element.onclick = function () {
        // Create a virtual link and click it
        var link = document.createElement('a');
        link.target = credits.target;
        link.href = credits.href;
        link.click();
      }
    }
  });

  // Set the theme as you like
  var options = Highcharts.setOptions({
    credits: {
      enabled: true,
      text: 'Freedomvote',
      href: sourceUrl,
      target: '_blank' // Now this works like on an <a> tag
    }
  })
})
