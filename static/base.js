$(document).ready(function() {
	var add_links = $(".add");
	for (link in add_links){
		$(link).click(function(){$(".pub_form").toggle()});
	}
});
