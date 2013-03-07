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
/*
  $('#quoteform').submit(function(e){
    console.log(e);
    $(this).validate(function(e){
      $.post($(this).attr('action'), $(this).serialize(), function(data, text){
        //this is what happens if the form submissino is successful
      $(this).valid(function(){
        $('#myModal').modal('show');
      });

        console.log(data);
      });

    });
  
      e.preventDefault();
  });
*/

/*  submitHandler: function(form){
    
    console.log('hiya');
    $('#myModal').modal('show');
    //form.submit();
  } */





