$(function(){

  $('#doit').hide();
  $('form').mouseenter(function(){
    $('#doit').show();
  });
  
  $('form').click(function(){
    $('#command').replaceWith("<h1 id='command'>That's right.</h1>");
  });

  $('form').keypress(function(){
    $('#command').replaceWith("<h1 id='command'>Just like that.</h1>");
  });
});






