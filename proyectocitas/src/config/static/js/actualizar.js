(function() {
    'use strict'
    const forms = document.querySelectorAll('.requires-validation')
    Array.from(forms)
        .forEach(function(form) {
            form.addEventListener('submit', function(event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
                const nombre = document.getElementById("name").value;
                const correo = document.getElementById("email").value;
                const password = document.getElementById("password").value;
                const telefono = document.getElementById("telefono").value;
                const direccion = document.getElementById("direccion").value;
                console.log(nombre, correo, password, telefono,direccion)
                axios
                .post(
                    '/api/actualizardatos', {
                        nombre: nombre,
                        correo: correo,
                        password: password,
                        telefono: telefono,
                        direccion: direccion,
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
                
      
            }, false)
        })
})();

(function($) {
    "use strict";

    $(function() {
        var header = $(".start-style");
        $(window).scroll(function() {
            var scroll = $(window).scrollTop();

            if (scroll >= 10) {
                header.removeClass('start-style').addClass("scroll-on");
            } else {
                header.removeClass("scroll-on").addClass('start-style');
            }
        });
    });

    //Animation

    $(document).ready(function() {
        $('body.hero-anime').removeClass('hero-anime');
    });

    //Menu On Hover

    $('body').on('mouseenter mouseleave', '.nav-item', function(e) {
        if ($(window).width() > 750) {
            var _d = $(e.target).closest('.nav-item');
            _d.addClass('show');
            setTimeout(function() {
                _d[_d.is(':hover') ? 'addClass' : 'removeClass']('show');
            }, 1);
        }
    });

    //Switch light/dark


    function a() {
        if ($("body").hasClass("dark")) {
            $("body").removeClass("dark");
        } else {
            $("body").addClass("dark");
        }
    };

})(jQuery);

