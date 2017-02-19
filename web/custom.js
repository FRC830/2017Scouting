$(function(){
    $('#scouting-form #defense').rules('add', {min: 1, max: 10});
    $('#comments').keyup(function(){
    	if ($('#comments').val().toLowerCase().indexOf("rainbow") != -1) {
    		$('.content').css('background','linear-gradient(to bottom, rgba(255,44,40,1) 0%,rgba(255,128,0,1) 17%,rgba(255,246,0,1) 34%,rgba(0,170,0,1) 50%,rgba(0,219,201,1) 66%,rgba(43,0,216,1) 83%,rgba(165,46,121,1) 100%)');
    	}
    	else {
    		$('.content').css('background','white');
    	}
    }
})
