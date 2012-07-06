(function() {
  /**
   * When the sign in button has been clicked, toggle showing the sign-in container.
   */
  function sign_in_click() {
    $('.sign-in-form').css('display', 'block');
  }
  
  $(function() {
    $('.sign-in').click(sign_in_click);
  });
}).apply(namespace('edu.biology.gatech'));
