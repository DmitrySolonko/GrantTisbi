$(document).ready(function() {
	$('.header__burger').click(function(event) {
		$('.header__burger,.header__menu').toggleClass('active');
		$('body').toggleClass('lock');
	});

	$('.slider').slick({
		arrows: false,
		dots: true,
		adaptiveHeight: true,
		autoplay: true,
  		autoplaySpeed: 4000,
	});
});


