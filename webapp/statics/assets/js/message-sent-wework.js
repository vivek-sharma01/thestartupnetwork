$(function () {
// Get the modal
var messageSentWeWorkmodal = $('#message-sent-wework');

// Get the button that opens the modal
var btn = $("#message-sent-popup");

// Get the <span> element that closes the modal
var span = $("#message-sent-wework-close");

// When the user clicks the button, open the modal 
btn.click(function() {
    messageSentWeWorkmodal.show();
});

// When the user clicks on <span> (x), close the modal
span.click(function() {
    messageSentWeWorkmodal.hide();
});

// When the user clicks anywhere outside of the modal, close it
window.onclick(function(event) {
    if (event.target == messageSentWeWorkmodal) {
        messageSentWeWorkmodal.hide();
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