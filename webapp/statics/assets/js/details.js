$(function () {



			var that = this;
			var toolitup = $(".rating-container").jRate({
				rating: 1,
				startColor: "#008489",
				endColor: "#008489",
				strokeColor: "#008489",
				strokeWidth:"20px",
				precision: 1,
				width: 22,
				height: 22
			});

			var toolitup = $(".price-rate").jRate({
				rating: 1,
				startColor: "#008489",
				endColor: "#008489",
				strokeColor: '#008489',
				strokeWidth:'20px',
				precision: 1,
				width: 15,
				height: 15,
			});



		$('.similar-types-coworks').slick({
		  infinite: true,
		  speed: 300,
		  slidesToShow: 4,
		  slidesToScroll: 4,
		  responsive: [
			{
			  breakpoint: 1024,
			  settings: "unslick",
			  settings: {
				slidesToShow: 4,
				slidesToScroll: 4,
				infinite: true,
				dots: true
			  }
			},
			{
			  breakpoint: 600,
			  settings: {
				slidesToShow: 2,
				slidesToScroll: 2
			  }
			},
			{
			  breakpoint: 480,
			  settings: {
				slidesToShow: 1,
				slidesToScroll: 1
			  }
			}
			// You can unslick at a given breakpoint now by adding:
			// settings: "unslick"
			// instead of a settings object
		  ]
		});

		$('.popular-cowork').slick({
		  infinite: true,
		  speed: 300,
		  slidesToShow: 3,
		  slidesToScroll: 3,
		  responsive: [
			{
			  breakpoint: 1024,
			  settings: "unslick",
			  settings: {
				slidesToShow: 3,
				slidesToScroll: 3,
				infinite: true,
				dots: true
			  }
			},
			{
			  breakpoint: 600,
			  settings: {
				slidesToShow: 2,
				slidesToScroll: 2
			  }
			},
			{
			  breakpoint: 480,
			  settings: {
				slidesToShow: 1,
				slidesToScroll: 1
			  }
			}
			// You can unslick at a given breakpoint now by adding:
			// settings: "unslick"
			// instead of a settings object
		  ]
		});


        var imageUrl = $('#image_url').val();
        $('#hero').css('background-image', 'url(' + imageUrl + ')');

});