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

        <!-- Read More Logic -->

        var showChar = 300;  // How many characters are shown by default
        var ellipsestext = "...";
        var moretext = "Read More";
        var lesstext = "Read less";

         $('.overview-summary p').each(function() {
            var content = $(this).html();

            if(content.length > showChar) {

                var c = content.substr(0, showChar);
                var h = content.substr(showChar, content.length - showChar);

                var html = c + '<span class="moreellipses">' + ellipsestext+ '&nbsp;</span><span class="morecontent"><span>'
                 + h + '</span>&nbsp;&nbsp;<a href="" class="overview-more">' + moretext +
                  '</a><img src="/statics/assets/images/down-arrow.png"></span>';

                $(this).html(html);
            }

        });

        $(".overview-more").click(function(){
            if($(this).hasClass("less")) {
                $(this).removeClass("less");
                $(this).html(moretext);
                $(".morecontent img").show();
            } else {
                $(this).addClass("less");
                $(this).html(lesstext);
                $(".morecontent img").hide();
            }
            $(this).parent().prev().toggle();
            $(this).prev().toggle();
            return false;
        });

        var scrollBottomValue;
		var footerHeight;

		var similarCoworks = $('.similar-coworks');
		var otherWeWorks = $('.other-weworks-section');
		var footerStart = $('.footer-start');

		if(similarCoworks.length){
			footerHeight = $('.similar-coworks').offset().top;
			scrollBottomValue = footerHeight - 600;
		}else if(otherWeWorks.length){
			footerHeight = $('.other-weworks-section').offset().top;
			scrollBottomValue = footerHeight - 600;
		}
		else{
			footerHeight = $('.footer-start').offset().top;
			scrollBottomValue = footerHeight - 600;
		}
		$(document).scroll(function(){
			if($(document).scrollTop() > 600 && $(document).scrollTop()< scrollBottomValue){
				$("#rightContent").addClass('fixedRightContent');
			}
			else{
				$("#rightContent").removeClass('fixedRightContent');
			}
		});




	var availablespace = $(".available-space").length;

	if(availablespace > 3){
		$(".more-spaces").show();
	}

	$(".available-space").slice(0,3).show();

	$(".more-spaces").click(function (event) {
	    $(".available-space").slice(3, 99).toggle();
	});


    var imageUrl = $('#image_url').val();
    $('#hero').css('background-image', 'url(' + imageUrl + ')');



});