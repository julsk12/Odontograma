let send = document.getElementById('pos');
function viewcards() {
    axios.get('/api/cards', {
        responseType: 'json'
    })
        .then(function (response) {
            let datos = response.data
            var length = (Object.keys(datos).length) + 1;
            let estaa = '';
            var numeros = [1, 2, 3, 4, 5, 6];
            for (let index = 1; index < length; index++) {
                estaa += `
                <div class="card" onclick="seleccionarTarjeta(this)">
                  <h3 class="title">${datos[index].nombre}</h3>
                  <div class="bar">
                    <div class="emptybar"></div>
                    <div class="filledbar"></div>
                  </div>
                  <div class="circle">
                    <img class="img" src="../../static/images/pic${numeros[index]}.jpg" alt="" />
                  </div>
                </div>`;
            }
            send.innerHTML = estaa

        })
        .catch(function (error) {
            console.log(error);
        });


}
window.addEventListener('load', function () {
    viewcards();
});



let id_odotologo;
function seleccionarTarjeta(tarjeta) {
    const tarjetas = document.querySelectorAll('.card');
    tarjetas.forEach(tarjeta => {
        tarjeta.classList.remove('selected');
    });

    // Agregar la clase "selected" a la tarjeta seleccionada
    tarjeta.classList.add('selected');

    // Obtener el caption de la tarjeta seleccionada
    id_odotologo = tarjeta.querySelector('.title').textContent;

    // Utiliza los valores del caption como desees
    console.log('Título:', id_odotologo);
}

function aggC() {
    const id_paciente = document.getElementById("identificacion").value;
    const fecha = document.getElementById("fecha").value;
    const hora = document.getElementById("hora").value;
    const nota = document.getElementById("especialidad").value;
    const sede = document.getElementById("sede").value;
    console.log(id_paciente, fecha, hora, nota, sede, id_odotologo);

    axios
        .post(
            '/api/guardarcitas', {
            id_paciente: id_paciente,
            nombreodonto: id_odotologo,
            fecha: fecha,
            hora: hora,
            nota: nota,
            sede: sede
        }, {
            headers: {
                'Content-Type': 'application/json'
            },
        }
        )
        .then((res) => {
            console.log(res.data);
            if (res === "bien") {
                window.location.href = "/fronted/indexpago"
            }
        })
        .catch((err) => {
            console.log(err);
        });
        
}

function validateForm() {
  // Obtener los valores de los campos
  var identificacion = document.getElementById("identificacion").value;
  var especialidad = document.getElementById("especialidad").value;
  var fecha = document.getElementById("fecha").value;
  var hora = document.getElementById("hora").value;
  var sede = document.getElementById("sede").value;

  // Realizar las validaciones
  if (identificacion === "") {
    alert("Por favor ingrese una identificación");
    return false; // Evita que se envíe el formulario
  }

  if (especialidad === "") {
    Swal.fire({
        title: 'Hay valores Vacios',
        text: 'Por favor ingrese una especialidad',
        imageUrl: 'https://www.latercera.com/resizer/sb91NqJC0m16VtB4cjbZvQxIEmc=/900x600/smart/arc-anglerfish-arc2-prod-copesa.s3.amazonaws.com/public/YPG2SOLGAJBDBHO5PRJA75IEGI.jpg',
        imageWidth: 200,
        imageHeight: 200,
        imageAlt: 'Custom image',
    })
    return false;
  }

  if (fecha === "") {
    Swal.fire({
        title: 'Hay valores Vacios',
        text: 'Por favor ingrese una fecha',
        imageUrl: 'https://www.latercera.com/resizer/sb91NqJC0m16VtB4cjbZvQxIEmc=/900x600/smart/arc-anglerfish-arc2-prod-copesa.s3.amazonaws.com/public/YPG2SOLGAJBDBHO5PRJA75IEGI.jpg',
        imageWidth: 200,
        imageHeight: 200,
        imageAlt: 'Custom image',
    })
    return false;
  }

  if (hora === "") {
    Swal.fire({
        title: 'Hay valores Vacios',
        text: 'Por favor ingrese una hora',
        imageUrl: 'https://www.latercera.com/resizer/sb91NqJC0m16VtB4cjbZvQxIEmc=/900x600/smart/arc-anglerfish-arc2-prod-copesa.s3.amazonaws.com/public/YPG2SOLGAJBDBHO5PRJA75IEGI.jpg',
        imageWidth: 200,
        imageHeight: 200,
        imageAlt: 'Custom image',
    })
    return false;
  }

  if (sede === "") {
    Swal.fire({
        title: 'Hay valores Vacios',
        text: 'Por favor ingrese una sede',
        imageUrl: 'https://www.latercera.com/resizer/sb91NqJC0m16VtB4cjbZvQxIEmc=/900x600/smart/arc-anglerfish-arc2-prod-copesa.s3.amazonaws.com/public/YPG2SOLGAJBDBHO5PRJA75IEGI.jpg',
        imageWidth: 200,
        imageHeight: 200,
        imageAlt: 'Custom image',
    })
    return false;
  }

  // Si todas las validaciones pasan, el formulario se envía
    aggC();

      // Si todas las validaciones pasan, redirigir al usuario
  window.location.href = "/fronted/indexpago";

  // Evita que se envíe el formulario de manera predeterminada
  return false
   
}


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
            var _d = $(e.target).closest('.nav-item');
            _d.addClass('show');
            setTimeout(function () {
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



