(function (){
  "use strict";

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      function getCookie(name) {
        var cookieValue = null
        if (document.cookie && document.cookie !== '') {
          var cookies = document.cookie.split(';')
          for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i])
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break;
            }
          }
        }
        return cookieValue;
      }
      if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'))
      }
    },
  })

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
    $('input[name="party_other"]').val('')
    $('input[name="party_other"]').hide()
  }

  $('select[name="party"]').on('change', function(){
    if ($(this).val() == 'party_other') {
      $('input[name="party_other"]').show()
    }
    else {
      $('input[name="party_other"]').val('')
      $('input[name="party_other"]').hide()
    }
  })

  $('.slider').on('slidechange', saveAnswer)
  $('.note').on('focusout', saveAnswer)

  function saveAnswer(e) {
    var form = $(e.target).closest('form')
    var slider = form.children('.slider')
    var value = slider.slider('value')
    form.find('input[name="agreement_level"]').val(value)

    $.post('/answer/', form.serialize())
  }

})();
