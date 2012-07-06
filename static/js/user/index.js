(function() {
  function create_user_click() {
    window.location = "/user/new";
  }
  
  $(function() {
    $("#create_user").click(create_user_click);
  });
}).apply(namespace('edu.gatech.biology'));