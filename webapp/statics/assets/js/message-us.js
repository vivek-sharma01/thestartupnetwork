$(document).ready(function() {
    // Get the modal

var messageModal = $('#contact-wework-modal');

// Get the button that opens the modal
var btn =$(".message-us-popup");

// Get the <span> element that closes the modal
var span = $(".contact-wework-close")[0];

// When the user clicks the button, open the modal
btn.click(function() {
    messageModal.show();
});

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    messageModal.hide();
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == messageModal) {
        messageModal.hide();
    }
}

// background-opacity

function dim(){
    document.body.style.backgroundColor = "rgba(219, 219, 219, 0.7)";
}

function transparent(){
    document.body.style.backgroundColor = "transparent";
}

var csrftoken = Cookies.get('csrftoken');

$('#contact-cowork-form').submit(function(e) {

        e.preventDefault();
        $form = $(this);
        data = {
            'name': $('#contact-name').val(),
            'email': $('#contact-email').val(),
            'phone': $('#contact-phone').val(),
            'message': $('#contact-message').val(),
            'cowork_slug': $('#cowork_slug').val()
        }
        $.ajax({
            type: "POST",
            url: '/contact-us-form/',
            data: JSON.stringify(data),
            headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
            },
            success: function(response) {
                messageModal.hide();
                var messageSentWeWorkmodal = $('#message-sent-wework');
                messageSentWeWorkmodal.show();
            },
            error: function (response) {
                messageModal.hide();
                var messageSentWeWorkmodal = $('#message-sent-wework');
                messageSentWeWorkmodal.show();

            },
            dataType: 'json',
            contentType: 'json'
        });

      });

});

