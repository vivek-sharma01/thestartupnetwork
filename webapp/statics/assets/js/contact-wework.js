$(function () {
    // Get the modal
    var contactWeWorkModal = $('#contact-wework-modal');

    // Get the button that opens the modal
    var btn = $("#contact-weWork");

    // Get the <span> element that closes the modal
    var span = $("#contact-wework-close");

    // When the user clicks the button, open the modal
    btn.click(function() {
        contactWeWorkModal.show();
    });

    // When the user clicks on <span> (x), close the modal
    span.click(function() {
        contactWeWorkModal.hide();
    });

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == contactWeWorkModal) {
            contactWeWorkModal.hide();
        }
    }

    // background-opacity

    function dim(){
        document.body.style.backgroundColor = "rgba(219, 219, 219, 0.7)";
    }

    function transparent(){
        document.body.style.backgroundColor = "transparent";
    }
    // country code

    function phone(){
        document.getElementById("code").value = "+91";
    }

});