$(document).ready(function() {
	var links = $(".add");
	for (var i=0; i < links.length; i++){
		$(links[i]).click(function(){$(".pub_form").toggle()});
	}
});
