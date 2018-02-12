$(function () {
// Get the modal

var addRatingModal = $('#add-cowork-modal');

// Get the button that opens the modal
var addRatingBtn = $('#add-rating-popup');

// Get the <span> element that closes the modal
var span = $(".add-cowork-rating-close");

// When the user clicks the button, open the modal 
addRatingBtn.click(function() {
    addRatingModal.show();
});

// When the user clicks on <span> (x), close the modal
span.click(function() {
    addRatingModal.hide();
});

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == addRatingModal) {
        addRatingModal.hide();
    }
}
});

$(document).on('click',".rating-selector",function(){
	
var rates = document.getElementsByName('rating');
var rate_value;
for(var i = 0; i < rates.length; i++){
    if(rates[i].checked){
        rate_value = rates[i].value;
         document.getElementById("selected-rating-value").innerHTML = rate_value;
    }
} 

$("#display-1").innerHTML = rate_value;
$("#submit-rating").disabled = false;
$("#submit-rating").show();
$("#submit-rating").css({"backgroundColor":"teal","color":"white"});
});

/* 
function myFunction() {
var rates = document.getElementsByName('rating');
var rate_value;
for(var i = 0; i < rates.length; i++){
    if(rates[i].checked){
        rate_value = rates[i].value;
         document.getElementById("selected-rating-value").innerHTML = rate_value;
    }
} 

document.getElementById("display-1").innerHTML = rate_value;
document.getElementById("submit-rating").disabled = false;
document.getElementById("submit-rating").style.display = "block";
document.getElementById("submit-rating").style.backgroundColor = "teal";
document.getElementById("submit-rating").style.color = "white";

} */

function selectRating() {
	$("#submit-rating").show();
}

function change() {
	$("#display").show();
	$("#rating-popup").hide();
}