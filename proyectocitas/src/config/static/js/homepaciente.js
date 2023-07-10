(function ($) {
	"use strict";

	$(function () {
		var header = $(".start-style");
		$(window).scroll(function () {
			var scroll = $(window).scrollTop();

			if (scroll >= 10) {
				header.removeClass('start-style').addClass("scroll-on");
			} else {
				header.removeClass("scroll-on").addClass('start-style');
			}
		});
	});

	//Animation

	$(document).ready(function () {
		$('body.hero-anime').removeClass('hero-anime');
	});

	//Menu On Hover

	$('body').on('mouseenter mouseleave', '.nav-item', function (e) {
		if ($(window).width() > 750) {
			var _d = $(e.target).closest('.nav-item'); _d.addClass('show');
			setTimeout(function () {
				_d[_d.is(':hover') ? 'addClass' : 'removeClass']('show');
			}, 1);
		}
	});

	//Switch light/dark

	$("#switch").on('click', function () {
		if ($("body").hasClass("dark")) {
			$("body").removeClass("dark");
			$("#switch").removeClass("switched");
		}
		else {
			$("body").addClass("dark");
			$("#switch").addClass("switched");
		}
	});





})(jQuery);


function cerrar_sesion() {
	const sesion = "sesion_cerrada"
	axios.post('/api/cerrar_sesion', {
	sesion : sesion
}, {
	headers: {
		'Content-Type': 'application/json'
	},
}
)
	.then((res) => {
		console.log(res.data);
	})
	.catch((err) => {
		console.log(err);
	});
}


document.addEventListener('mousemove', function(event) {
  movimiento();
});

function movimiento() {
	movi = "se movio"
	axios.post('/api/movimiento', {
	movi : movi
}, {
	headers: {
		'Content-Type': 'application/json'
	},
}
)
	.then((res) => {
		if (res.data === "algo") {
			window.location.href = "/"
		}

	})
	.catch((err) => {
		console.log(err);
	});
}