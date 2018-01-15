$(function()
{

	$('#city-select').on('change', function() {
	    var city_url = $("#city-select option:selected"). val();
	    window.location.href = city_url;
	})
});