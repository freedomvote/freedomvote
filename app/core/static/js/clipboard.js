$(document).ready(function copToClipboard() {
  let menuButton = document.getElementById('share_opinion')
  menuButton.addEventListener('click', clipboardButton)

  function clipboardButton() {
    let clipboardButton = document.getElementById('clip')
    clipboardButton.addEventListener('click', addToClipboard)

    function addToClipboard() {
      let opinionLink = document.getElementById('opinion_link')
      opinionLink.focus()
      opinionLink.select()
      document.execCommand('copy')
    }
  }
})
