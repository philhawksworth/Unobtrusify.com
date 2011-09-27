/*
	http://unobtrusify.com

	Hello there!  Thanks for coming over to look at the Javascript. You are most welcome.
	You can see more examples of good Unobtrusive Javascript over at http://jquery.com
	Good luck with your unobtrusifying!
	- Phil 
	- http://hawksworx.com
	- http://twitter.com/philhawksworth
*/

$(document).ready(function(){
	$('#wrapper > div').hide().css({opacity:0});
	$('#wrapper > a').
		addClass('clickable').
		click(function(){				
			toggleSection($(this).next());
			$(this).blur();
			return false;
		}).
		keypress(function(e){
			if(e.which == 13){
				toggleSection($(e.target).next());
				$(this).blur();
			}
		});
});

function toggleSection(section){
	if(section.is(':visible')){
		section.animate( {opacity:0}, 300 );
		section.slideUp(300);
	} else {
		section.slideDown(150);
		section.animate( {opacity:1}, 300);
	}	
}