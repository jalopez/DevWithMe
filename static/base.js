$(document).ready(function() {
	var links = $(".addSnippet");
	for (var i=0; i < links.length; i++){
		$(links[i]).click(function(){$(".snippet_form").toggle()});
	}
	
	var links = $(".addReply");
	for (var i=0; i < links.length; i++){
		$(links[i]).click(function(){$(".reply_form").toggle()});
	}
	
	var links = $(".addRelationship");
	for (var i=0; i < links.length; i++){
		$(links[i]).click(function(){$(".relationship_form").toggle()});
	}
});
