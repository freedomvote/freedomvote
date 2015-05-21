jQuery(function() {
  'use strict'

  $(document).on('click', '.desc-toggler:not(.no-desc)', function() {
    var desc = $(this).parent().find('.desc')
    console.log(desc)

    desc.toggleClass('desc-shown')
  })
})
