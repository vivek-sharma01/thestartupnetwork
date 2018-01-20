$(function()
{

	$('#city-select').on('change', function() {
	    var city_url = $("#city-select option:selected"). val();
	    window.location.href = city_url;
	});

	$('#search-coworks-button').on('click', function() {
	    var search_url = '/coworks/?search=' + $("#search-coworks-input").val();
	    window.location.href = search_url;
	});

});