jQuery(function() {
  'use strict'

  var langForm = $('.language')

  langForm.on('click', 'a', function(e) {
    e.preventDefault()
    var link = $(e.target)
    langForm.find('input[name="language"]').val(link.data('lang'))
    langForm.submit()
  })
})
