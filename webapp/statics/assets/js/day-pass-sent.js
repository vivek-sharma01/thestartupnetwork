
// Get the modal
var dayPassSentModal = $('#day-pass-request-sent');

// Get the button that opens the modal
//var btn = $("#book-tour-popup");

// Get the <span> element that closes the modal
var span = $(".day-pass-request-sent-close")[0];

// When the user clicks the button, open the modal 
//btn.onclick = function() {
//    dayPassSentModal.style.display = "block";
//}

// When the user clicks on <span> (x), close the modal
span.click(function() {
    dayPassSentModal.hide();
});

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == dayPassSentModal) {
        dayPassSentModal.style.display = "none";
    }
}

// background-opacity

function dim(){
    document.body.style.backgroundColor = "rgba(219, 219, 219, 0.7)";
}

function transparent(){
    document.body.style.backgroundColor = "transparent";
}
