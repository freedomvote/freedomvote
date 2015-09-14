jQuery(function() {
  'use strict'

  $('.readonly-slider').each(function() {
    initSlider($(this))
  })

  function initSlider(obj) {
    var own        = obj.children('.readonly-slider-own')
    var politician = obj.children('.readonly-slider-politician')

    var politicianLeft = parseInt(politician.data('value')) * 10

    politician.animate({ 'left': politicianLeft + '%' }, 'slow')
    politician.popover({
      title: politician.data('title'),
      content: politician.data('text'),
      container: 'body',
      trigger: 'hover',
      placement: 'top'
    })

    if (own.length) {
      var ownLeft = parseInt(own.data('value')) * 10
      own.animate({ 'left': ownLeft + '%' }, 'slow')
      own.popover({
        title: own.data('title'),
        content: own.data('text'),
        container: 'body',
        trigger: 'hover',
        placement: 'top'
      })
    }
  }

})
