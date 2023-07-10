function viewprueba() {
  let send = document.getElementById('sal');
  axios.get('consultargrama', {
    responseType: 'json'
  })
    .then(function (response) {
      let datos = response.data
      var length = (Object.keys(datos).length) + 1;
      let estaa = '';
      for (let index = 1; index < length; index++) {
        estaa += `<div class="card1" onclick="seleccionarTarjeta(this)">
                <h3 class="title">${datos[index].id}</h3>
                <h3 class="caption">${datos[index].nombre}</h3>
                <h3 class="sub">${datos[index].email}</h3>
                <div class="bar">
                    <div class="emptybar"></div>
                    <div class="filledbar"></div>
                </div>
                <div class="circle">
                
                </div>
                </div> `;
      }
      send.innerHTML = estaa

    })
    .catch(function (error) {
      console.log(error);
    });


}
window.addEventListener('load', function () {
  viewprueba();
});

let id_paciente;
function seleccionarTarjeta(tarjeta) {
  const tarjetas = document.querySelectorAll('.card1');
  const caption = document.querySelectorAll('.caption');
  const title = document.querySelectorAll('.title');
  const sub = document.querySelectorAll('.sub');

  // Remover la clase "selected" de todas las tarjetas
  tarjetas.forEach((tarjeta) => {
    tarjeta.classList.remove('selected');
  });

  // Agregar la clase "selected" a la tarjeta seleccionada
  tarjeta.classList.add('selected');

  // Obtener el caption de la tarjeta seleccionada
  id_paciente = tarjeta.querySelector('.title').textContent;

  // Utiliza los valores del caption como desees
  console.log('Título:', id_paciente);

  axios
  .post('/api/seleccionarcita', {
    id_paciente: id_paciente,
  })
  .then((response) => {
    console.log(response.data);
    console.log(response.data.message === 'Seleccion exitosa')

    if (response.data.message === 'Seleccion exitosa') {
      Swal.fire({
        title: '¡Informacion enviada con éxito!',
        icon: 'success',
      });

      // Obtener los datos del paciente aquí antes de redireccionar
      axios
        .post('/api/datospaciente', {
          id_paciente: id_paciente,
          responseType: 'json',
        })
        .then(function (response) {
          let datos = response.data;
          console.log(datos);

          // Redireccionar a la página de destino con los datos del paciente como parámetros
          const url = `/fronted/IndexOdontograma?id=${datos.id}&nombre=${datos.nombre}`;
          setTimeout(function() {
              window.location.href = url;
            }, 1500);
          const evento = new Event('pacienteenviado');
          console.log("Evento pacienteenviado disparado");
          window.dispatchEvent(evento);
        })
        .catch(function (error) {
          console.log(error);
        });
    } else {
      Swal.fire({
        title: 'Error al enviar datos',
        icon: 'error',
      });
    }
  })
  .catch((error) => {
    console.error(error);
  });
}

// window.addEventListener('load', function () {
//   mostrarpaciente();
// });
// function mostrarpaciente() {
//   const datospaciente = document.getElementById('paciente');
//   axios.post('/api/datospaciente', {
//     responseType: 'json'
//   }).then(function (response) {

//     let datos = response.data;
//     console.log(datos)
//     // let informacion = '';
//     // informacion =`<p class="text-center info" id="iduser">${datos.id}</p>
//     // <p class="identificacion" value="" id="nameuser">${datos.nombre}</p>`;
//     // datospaciente.innerHTML += informacion;
//     document.getElementById('iduser').innerText = datos.id;
//     document.getElementById('nameuser').innerText = datos.nombre;
//     const evento = new Event('pacienteCargado');
//     console.log("Evento pacienteCargado disparado");
//     window.dispatchEvent(evento);
//   })
//     .catch(function (error) {
//       console.log(error);
//     });
// }
function viewbuscar() {
  const busca = document.getElementById('busca').value;
  console.log(busca);
  const pattern = /^[A-Za-z\sáéíóúÁÉÍÓÚ]+$/;
  if (pattern.test(busca)) {
    viewnombre();
    alert("aquí no es");
  } else {
    viewid();
    alert("estoy entrando en el else");
  }
}
function viewid() {
  let send = document.getElementById('sal');
  const busca = document.getElementById('busca');

  axios.post('consultabusqueda', {
    busca: busca.value,
    responseType: 'json'
  })
    .then(function (response) {
      let datos = response.data
      var length = (Object.keys(datos).length) + 1;
      let estaa = '';
      for (let index = 1; index < length; index++) {
        estaa += `<div class="card1" onclick="seleccionarTarjeta(this)">
                <h3 class="title">${datos[index].id}</h3>
                <h3 class="caption">${datos[index].nombre}</h3>
                <h3 class="sub">${datos[index].email}</h3>
                <div class="bar">
                    <div class="emptybar"></div>
                    <div class="filledbar"></div>
                </div>
                <div class="circle">
                
                </div>
                </div> `;
      }
      send.innerHTML = estaa

    })
    .catch(function (error) {
      console.log(error);
    });


}
function viewnombre() {
  let send = document.getElementById('sal');
  const busca = document.getElementById('busca');
  console.log(busca);
  axios.post('consultanombre', {
    busca: busca.value,
    responseType: 'json'
  })
    .then(function (response) {
      let datos = response.data
      var length = (Object.keys(datos).length) + 1;
      let estaa = '';
      for (let index = 1; index < length; index++) {
        estaa += `<div class="card1" onclick="seleccionarTarjeta(this)">
                <h3 class="title">${datos[index].id}</h3>
                <h3 class="caption">${datos[index].nombre}</h3>
                <h3 class="sub">${datos[index].email}</h3>
                <div class="bar">
                    <div class="emptybar"></div>
                    <div class="filledbar"></div>
                </div>
                <div class="circle">
                
                </div>
                </div> `;
      }
      send.innerHTML = estaa

    })
    .catch(function (error) {
      console.log(error);
    });


}
