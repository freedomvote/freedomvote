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

  $('#form').submit(function(e){
    $('.slider').each(function(){
      var input = $(this).parent().children('input:hidden')
      input.val($(this).slider('value'))
    })
  })
});
