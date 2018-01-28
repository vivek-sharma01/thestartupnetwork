$(function() {

	$('#message-us-form').submit(function(e) {
        e.preventDefault();
        $form = $(this);
        $.ajax({
            type: "POST",
            url: '/subscribe/',
            data: {'email': $('#message-us-email').val()},
            success: function(response) {
                $('#subscribe-success').text('subscribed successfully');
                setTimeout(function(){ $('#subscribe-success').text(''); }, 3000);

            },
            error: function (response) {
                $('#subscribe-error').text('Already subscribed');
                setTimeout(function(){  $('#subscribe-error').text('');}, 3000);

            },
            dataType: 'json'
        });

      });
});