$(function () {
// Get the modal
var modal = $('#myModal');

// Get the button that opens the modal
var btn = $("#add-coWork");

// Get the <span> element that closes the modal
var span = $(".close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
    modal.show();
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.hide();
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.hide();
    }
}

// pop up close

function phone(){
    document.getElementById("code").value = "+91";
}

});
