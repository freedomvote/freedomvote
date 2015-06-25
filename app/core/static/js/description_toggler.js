jQuery(function() {
  'use strict'

  $(document).on('click', '.desc-toggler:not(.no-desc)', function() {
    $(this).parent().find('.desc').slideToggle()
  })
})
