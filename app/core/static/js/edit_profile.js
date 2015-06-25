jQuery(function ($){
  "use strict";
  var other_party = $('#id_party_other')
  var party = $('#id_party')
  var toggler = $('#toggle-party')

  other_party.toggle(party.val() === '' && other_party.val() !== '')

  toggler.on('click', function(){
    other_party.slideToggle()
  })

  party.on('change', function(){
    if (party.val() !== '')
      other_party.slideUp()
  })

  $('#links').on('click', '#link input[type="submit"]', function(e) {
    e.preventDefault()

    var form = $(e.target).closest('form')
    $.post(
        form.attr('action'),
        form.serialize(),
        function(data){
            $('#links').html(data)
        }
    )
  })

  $('#links').on('click', '.fa-trash', function(e) {
    e.preventDefault()

    var form = $(e.target).closest('form')
    $.post(
        form.attr('action'),
        form.serialize(),
        function(data){
            $('#links').html(data)
        }
    )
  })
});
