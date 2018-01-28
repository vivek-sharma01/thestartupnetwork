$(function () {
// Get the modal
var enquirySentModal = $('#enquiry-sent');

// Get the button that opens the modal
var btn = $("#enquiry-sent-popup");

// Get the <span> element that closes the modal
var span = $("#enquiry-sent-close");

// When the user clicks the button, open the modal 
btn.click(function() {
    enquirySentModal.show();
});

// When the user clicks on <span> (x), close the modal
span.click(function() {
    enquirySentModal.hide();
});

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == enquirySentModal) {
        enquirySentModal.hide();
    }
}

// background-opacity

function dim(){
    document.body.style.backgroundColor = "rgba(219, 219, 219, 0.7)";
}

function transparent(){
    document.body.style.backgroundColor = "transparent";
}

});