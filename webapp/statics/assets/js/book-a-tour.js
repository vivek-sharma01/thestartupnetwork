$(function () {

var selectedSlot;

var bookTourModal = $('#book-a-tour');

// Get the button that opens the modal
var bookTourBtn = $("#book-tour-popup");

// Get the <span> element that closes the modal
var span = $(".book-a-tour-close");

// When the user clicks the button, open the modal 
bookTourBtn.click(function() {
    bookTourModal.show();
});

// When the user clicks on <span> (x), close the modal
span.click(function() {
    bookTourModal.hide();
});

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == bookTourModal) {
        bookTourModal.hide();
    }
}

// visibity function

$(document).on('click',"#time",function(){
	$('#time-slots').toggle();
});

$(document).on('click',".select-slot",function(){
	selectedSlot = $(this).attr('data-slot');
	$('#time').val(selectedSlot);
	
});

$(document).on('click',".fa-clock-o",function(){
	$('#time-slots').toggle();
});

// pop up show

function phone(){
    document.getElementById("code").value = "+91";
}

var sentModal = $('#tour-booked');
var span = $('#tour-booked-close');
span.click(function() {
    sentModal.hide();
});

var csrftoken = Cookies.get('csrftoken');
	$('#book-a-tour').submit(function(e)
      {
        e.preventDefault();
        $form = $(this);

        var data = {
            'name': $('#book-tour-name').val(),
            'email': $('#book-tour-email').val(),
            'phone': $('#book-tour-phone').val(),
            'message': $('#book-tour-message').val(),
            'reason': 'book a tour',
			'request_date':$('#book-a-tour-date').val() + 'T00:00',
			'cowork_slug': $('#cowork_slug').val(),
			'metadata': {
			    'timeslot': selectedSlot
			}

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
                bookTourModal.hide();
                sentModal.show();

            },
            error: function (response) {
                bookTourModal.hide();
                sentModal.show();
            },
            dataType: 'json',
            contentType: 'json'
        });

      });

});