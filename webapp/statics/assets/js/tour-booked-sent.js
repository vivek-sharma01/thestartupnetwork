$(function () {
// Get the modal
var tourBookedModal = $('#tour-booked');

// Get the button that opens the modal
var btn = $("#message-sent-popup");

// Get the <span> element that closes the modal
var span = $(".tour-booked-close")[0];

// When the user clicks the button, open the modal 
btn.click(function() {
    tourBookedModal.style.display = "block";
});

// When the user clicks on <span> (x), close the modal
span.click(function() {
    tourBookedModal.style.display = "none";
});

// When the user clicks anywhere outside of the modal, close it
window.onclick(function(event) {
    if (event.target == tourBookedModal) {
        tourBookedModal.style.display = "none";
    }
});

// background-opacity

function dim(){
    document.body.style.backgroundColor = "rgba(219, 219, 219, 0.7)";
}

function transparent(){
    document.body.style.backgroundColor = "transparent";
}




});