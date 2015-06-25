jQuery(function() {
  'use strict';

  $('.clipboard').on('click', function(e) {
    e.preventDefault()
    $('.clipboard-modal').find('#url').val($(this).data('clipboard-text'))
    $('.clipboard-modal').modal('show')
  })
})
