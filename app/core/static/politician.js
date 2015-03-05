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

  if ($('select[name="party"]').val() != 'party_other') {
    $('input[name="party_other"]').val('').hide()
  }

  $('select[name="party"]').on('change', function(){
    if ($(this).val() == 'party_other') {
      $('input[name="party_other"]').show()
    }
    else {
      $('input[name="party_other"]').val('').hide()
    }
  })

  $('.slider').on('slidechange', saveAnswer)
  $('.note').on('focusout', saveAnswer)

  function saveAnswer(e) {
    var form = $(e.target).closest('form')
    var slider = form.children('.slider')
    var value = slider.slider('value')
    form.find('input[name="agreement_level"]').val(value)

    $.post(Urls.politician_answer(), form.serialize())
  }

});
