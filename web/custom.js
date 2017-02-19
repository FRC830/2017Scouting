$(function(){
	alert($('#match_id').val());
    $('#scouting-form #defense').rules('add', {min: 1, max: 10});
})
