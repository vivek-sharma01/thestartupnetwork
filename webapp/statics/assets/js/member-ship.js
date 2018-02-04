$(function () {
// Get the modal
var membershipModal = $('#membership-enquiry-modal');

// Get the button that opens the modal
var btn = $("#member-ship");

// Get the <span> element that closes the modal
var span = $("#membership-close");

// When the user clicks the button, open the modal 
btn.click(function() {
    membershipModal.show();
});

// When the user clicks on <span> (x), close the modal
span.click(function() {
    membershipModal.hide();
});

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == membershipModal) {
        membershipModal.hide();
    }
}

function dim(){
    document.body.style.backgroundColor = "rgba(219, 219, 219, 0.7)";
}

function transparent(){
    document.body.style.backgroundColor = "transparent";
}

function phone(){
    document.getElementById("phone").value = "+91";
}

var sentModal = $('#enquiry-sent');
var span = $('#enquiry-sent-close');
span.click(function() {
    sentModal.hide();
});

var csrftoken = Cookies.get('csrftoken');
	$('#membership-enquiry-form').submit(function(e)
      {
        e.preventDefault();
        $form = $(this);

        var data = {
            'name': $('#name').val(),
            'email': $('#email').val(),
            'phone': $('#phone').val(),
            'message': $('#message').val(),
            'reason': 'membership enquiry'
        }

        $.ajax({
            type: "POST",
            url: '/contact-us-form/',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
                },
            data: JSON.stringify(data),
            success: function(response) {
                membershipModal.hide();
                sentModal.show();

            },
            error: function (response) {
                membershipModal.hide();
                sentModal.show();
            },
            dataType: 'json',
            contentType: 'json'
        });

      });

});