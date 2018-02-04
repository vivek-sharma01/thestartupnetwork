// Get the modal

$('.form_date').datetimepicker({
        language:  'en',
		startDate: new Date(),
        weekStart: 1,
        todayBtn:  1,
		autoclose: 1,
		todayHighlight: 1,
		startView: 2,
		minView: 2,
		forceParse: 0,
		pickerPosition: 'bottom-left'
});

var dayPassModal = $('#day-pass');

// Get the button that opens the modal
var btn = $("#day-pass-button");

// Get the <span> element that closes the modal
var span = $("#day-pass-close");

// When the user clicks the button, open the modal 
btn.click(function() {
    dayPassModal.show();
});

// When the user clicks on <span> (x), close the modal
span.click(function() {
    dayPassModal.hide();
});

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == dayPassModal) {
        dayPassModal.hide();
    }
}

function phone(){
    document.getElementById("code").value = "+91";
}

var dayPassSentModal = $('#day-pass-request-sent');
var span = $("#day-pass-request-sent-close");
span.click(function() {
    dayPassSentModal.hide();
});

var csrftoken = Cookies.get('csrftoken');
$('#day-pass-contact-us-button').on('click', function(e) {
        e.preventDefault();
        $form = $(this);

        var data = {
            'name': $('#day-pass-name').val(),
            'email': $('#day-pass-email').val(),
            'phone': $('#day-pass-phone').val(),
            'message': $('#day-pass-message').val(),
            'reason': 'day pass',
            'request_date': $('#day-pass-date').val() + 'T00:00',
            'cowork_slug': $('#cowork_slug').val()
        }
        console.log(data);
        $.ajax({
            type: "POST",
            url: '/contact-us-form/',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
                },
            data: JSON.stringify(data),
            success: function(response) {
                dayPassModal.hide();
                dayPassSentModal.show();

            },
            error: function (response) {
                dayPassModal.hide();
                dayPassSentModal.show();

            },
            dataType: 'json',
            contentType: 'json'
        });

});