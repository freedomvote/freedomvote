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
    $.post(
        Urls.add_link(),
        $(e.target).closest('form').serialize(),
        function(data){
            $('#links').html(data)
        }
    )
  })

  $('#links').on('click', '.glyphicon-trash', function(e) {
    e.preventDefault()
    $.post(
        Urls.delete_link(),
        $(e.target).closest('form').serialize(),
        function(data){
            $('#links').html(data)
        }
    )
  })
});
