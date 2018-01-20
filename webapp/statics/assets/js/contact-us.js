$(function()
{

	$('#contact-us-button').on('click', function(e)
      {
        e.preventDefault();
        $form = $(this);

        var data = {
            'name': $('#name').val(),
            'email': $('#email').val(),
            'phone': $('#phone').val(),
            'message': $('#message').val(),
        }

        $.ajax({
            type: "POST",
            url: '/contact-us-form/',
            headers: {

                'Content-Type': 'application/json'
                },
            data: data,
            success: function(response) {
                $('#success').text('we will contact you shortly');
                setTimeout(function(){ $('#success').text(''); }, 3000);

            },
            error: function (response) {
                $('#error').text('something wrong occured');
                setTimeout(function(){  $('#-error').text('');}, 3000);

            },
            dataType: 'json'
        });

      });
});