FREEDOMVOTE.Socialmedia = {}

jQuery(function($) {
  'use strict'

  var socialnetwork = {
    facebook: {
      domain: 'facebook.com',
      name: 'Facebook',
      icon: 'fa-facebook-official'
    },
    twitter: {
      domain: 'twitter.com',
      name: 'Twitter',
      icon: 'fa-twitter'
    },
    instagram: {
      domain: 'instagram.com',
      name: 'Instagram',
      icon: 'fa-instagram'
    },
    linkedin: {
      domain: 'linkedin.com',
      name: 'Linkedin',
      icon: 'fa-linkedin-square'
    },
    xing: {
      domain: 'xing.com',
      name: 'Xing',
      icon: 'fa-xing-square'
    },
    telegram: {
      domain: 'telegram.com',
      name: 'Telegram',
      icon: 'fa-telegram'
    },
    pinterest: {
      domain: 'pinterest.com',
      name: 'Pinterest',
      icon: 'fa-pinterest-square'
    },
    fallback: {
      domain: 'fallback',
      name: 'Fallback',
      icon: 'fa-external-link'
    }
  }

  FREEDOMVOTE.Socialmedia.render = function() {
    $('.socialmedia-link').each(function(index) {
      var socialmediaItem = $(this),
        socialmediaItemIcon = socialmediaItem.find('.socialmedia-link-icon'),
        socialmediaItemAnchor = socialmediaItem.find('.socialmedia-link-anchor'),
        socialmediaItemUrl = socialmediaItemAnchor.attr('href'),
        baseUrl = getBaseUrl(socialmediaItemUrl),
        name,
        icon
      if (baseUrl) {
        var url = baseUrl[1],
          key = _.findKey(socialnetwork, {
            domain: url
          })
        if (key) {
          name = socialnetwork[key].name
          icon = socialnetwork[key].icon
        }
      }
      if (_.isEmpty(name) && _.isEmpty(icon)) {
        name = socialmediaItemUrl
        icon = socialnetwork.fallback.icon
      }
      socialmediaItemAnchor.text(name)
      socialmediaItemIcon.addClass(icon)
    })
  }

  function getBaseUrl(url) {
    var regex = new RegExp(/^https?:\/\/[w.]*([0-9a-z_][0-9a-z._-]*[0-9a-z])\/?/)
    return regex.exec(url)
  }
  FREEDOMVOTE.Socialmedia.render()
})
