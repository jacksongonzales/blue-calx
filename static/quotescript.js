$(function() {

var int=self.setInterval(function(){refreshQuote()},15000);
var refreshQuote = function(){
	$.ajax({
		url: "/quotes/randquo/",
		success: function(jsondata){
			var text = jsondata[0].fields.text, 
			who = jsondata[0].fields.who_said_it;
			$("#quotebox").fadeOut('slow').fadeIn('slow');
			$("#words").fadeOut('slow', function() {
				$(this).text(text).fadeIn("slow");
			});
			$("#attribution").fadeOut('slow', function() {
				$(this).html('-<em>' + who + '</em>').fadeIn("slow");
			});
		}
	});
}

});




