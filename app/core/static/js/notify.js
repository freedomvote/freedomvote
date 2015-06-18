$(function() {
  "use strict";

  $.addNotification = function(params) {
    var defaults = {
        'type' : 'info',
        'text' : '',
    }
    var options = $.extend({}, defaults, params || {});

    var elem = $('<div class="alert alert-'+options.type+'">'+options.text+'</div>')

    var messages = $('#messages')
    if (messages.length === 0) {
      messages = $('body').append('<div id="messages"></div>')
    }
    messages.append(elem)
    elem.notify()
  }

  $.fn.notify = function(params) {
    var defaults = {
        'timeout' : 10000,
        'clickable' : true,
        'opacity': 1,
        'opacity_hover': 0.7
    }
    var options = $.extend({}, defaults, params || {});

    if (options.clickable) {
      this.on('click', function(){$(this).slideUp()})
    }
    this.on('mouseover', function(){
      $(this).css({
        'opacity':options.opacity_hover,
        'cursor':'pointer'
      })
    })
    this.on('mouseleave', function(){
      $(this).css({
        'opacity':options.opacity,
        'cursor':'default'
      })
    })

    setTimeout(function(){
      $(this).fadeOut('fast')
    }.bind(this), options.timeout)
  }

  $('#messages').children().each(function() {
    $(this).notify()
  })
});
