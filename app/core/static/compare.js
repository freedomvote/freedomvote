jQuery(function ($){
  "use strict";

  $('.slider').each(function() {
    var value = $(this).data('value')
    $(this).slider({
      max: 10,
      min: 0,
      value: value,
      step: 2
    })
  })

  $('.slider').slider({
    'change': function(){
      $('#evaluate').addClass('disabled')
    }
  })

  $('#form').submit(function(e){
    $('.slider').each(function(){
      var input = $(this).prev('input:hidden')
      input.val($(this).slider('value'))
    })
  })
});
