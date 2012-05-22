mm = {};

(function() {
  $(function() {
    $("table tr").css("vertical-align", "top");
  
    $("#show").click(function() {
      var initial_substrate = $("input[name=initial_substrate]").val();
      var initial_enzyme = $("input[name=initial_enzyme]").val();
      $(".results").empty();
      
      $.ajax('/show/', {
        type: 'post',
        dataType: 'json',
        data: {
          initial_substrate: initial_substrate,
          initial_enzyme: initial_enzyme
        }
      }).success(function(data, status) {
        var img1 = $("<img/>").attr("src", "/static/" + data.figure_1);
        var img2 = $("<img/>").attr("src", "/static/" + data.figure_2);
        var img3 = $("<img/>").attr("src", "/static/" + data.figure_3);
        
        $(".results").append(img1);
        $(".results").append(img2);
        $(".results").append(img3);
      });
    });
  });
}).apply(mm);
