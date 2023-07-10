function expandirInformacion(element) {
  var contenidoAdicional = element.parentElement.nextElementSibling;
  if (contenidoAdicional.style.display === "none") {
    contenidoAdicional.style.display = "block";
    element.textContent = "-";
  } else {
    contenidoAdicional.style.display = "none";
    element.textContent = "+";
  }
}

function guardardiente() {
  const iduser = document.getElementById('iduser').innerText;
  const numerodiente = document.getElementById('numerodiente');
  const secciondiente = document.getElementById('secciondiente');
  const estadodiente = document.getElementById('estadodiente');
  const observaciondiente = document.getElementById('observaciondiente');
  const Tratamiento = document.getElementById('tratamiento').value;
  const fecha = document.getElementById('fecha');
  const selectElements = document.querySelectorAll('.form-select');
  console.log(iduser)

  axios.post('/api/savedientes', {
    iduser: iduser,
    numerodiente: numerodiente.value,
    secciondiente: secciondiente.value,
    estadodiente: estadodiente.value,
    observaciondiente: observaciondiente.value,
    Tratamiento: Tratamiento,
    fecha: fecha.value
}).then((response) => {
  console.log(response.data)

  if (response.data.message === 'Registro de datos exitoso') {
    Swal.fire({
      title: '¡Informacion guardada con éxito!',
      icon: 'success'
    });
  mostrarregistrodiente()
  for (let i = 0; i < selectElements.length; i++) {
    selectElements[i].value = 0;
  }
  observaciondiente.value = "";
  fecha.value = "";
  } else {
    Swal.fire({
      title: 'Error al guardar datos',
      icon: 'error'
    });
  }
})
    .catch((error) => {
        console.error(error)
    })
}

function selectColor(part, color) {
  const iduser = document.getElementById('iduser').innerText;
  if (color === '8' || color === '7' || color === '6') {
    const toothNumber = part.toothNumber;
    const tooth = document.querySelector(`.tooth[value="${toothNumber}"]`);
    const allParts = tooth.querySelectorAll('.tooth-part');

    allParts.forEach((p) => {
      const partNumber = p.getAttribute('data');
      const data = {
        iduser: iduser,
        toothNumber: toothNumber,
        partNumber: partNumber,
        color: color
      };

      axios.post('/api/savecolor', data)
        .then((response) => {

          if (response.data.message === 'Error al guardar los datos') {
            Swal.fire({
              title: 'Error al guardar datos',
              icon: 'error'
            });
          }
        })
        .catch((error) => {
          console.error('Error al guardar los datos:', error);
          // Manejar el error de alguna manera apropiada
        });
    });
  }else if(color === '9'){
    const data = {
      iduser: iduser,
      toothNumber: part.toothNumber
    };

    axios.post('/api/eliminardiente', data)
    .then((response) => {
      console.log(response.data);
    })
    .catch((error) => {
      console.error('Error al guardar los datos:', error);
      // Manejar el error de alguna manera apropiada
    });
  } else {
    const data = {
      iduser: iduser,
      toothNumber: part.toothNumber,
      partNumber: part.partNumber,
      color: color
    };

    axios.post('/api/savecolor', data)
      .then((response) => {
        console.log(response.data);
        if (response.data.message === 'Error al guardar los datos') {
          Swal.fire({
            title: 'Error al guardar datos',
            icon: 'error'
          });
        }
      })
      .catch((error) => {
        console.error('Error al guardar los datos:', error);
        // Manejar el error de alguna manera apropiada
      });
  }
}

// Función para obtener los colores desde la API
function obtenerColoresFromAPI() {
  const iduser = document.getElementById('iduser').innerText;
  console.log(iduser)
  axios.get('/api/getcolores', {
    params: {
      iduser: iduser
    }
  })
    .then(function (response) {
      const data = response.data;
      for (items in data) {
          const toothNumber = data[items].toothNumber;
          const partNumber = data[items].partNumber;
          const color = data[items].color;
        
          const part = document.querySelector(
          `.tooth[value="${toothNumber}"] .tooth-part[data="${partNumber}"]`
          );
        
          if (part) {
          part.style.backgroundColor = getColorValue(color);
          part.setAttribute('data-color', color);
          }
      }
      console.log(data)
      // Guardar los datos en la variable savedData
    })
    .catch(function (error) {
      console.error('Error al obtener los colores:', error);
    });
}

function getColorValue(color) {
  const colorMapping = {
    '1': 'red',
    '2': 'yellow',
    '3': 'orange',
    '4': 'tomato',
    '5': '#CC6600',
    '6': '#CC66CC',
    '7': 'green',
    '8': 'blue',
  };

  if (colorMapping.hasOwnProperty(color)) {
    return colorMapping[color];
  } else {
    return 'white';
  }
}
function mostrarpaciente() {
  // Obtener los parámetros de la URL
  const urlParams = new URLSearchParams(window.location.search);
  const pacienteId = urlParams.get('id');
  const pacienteNombre = urlParams.get('nombre');

  // Utilizar los parámetros en la función mostrarpaciente()
  console.log('ID del paciente:', pacienteId);
  console.log('Nombre del paciente:', pacienteNombre);
  document.getElementById('iduser').innerText = pacienteId;
  document.getElementById('nameuser').innerText = pacienteNombre;
}

document.addEventListener('DOMContentLoaded', function() {
  mostrarpaciente();
  mostrarregistrodiente();
  obtenerColoresFromAPI();
});
function mostrarregistrodiente() {
  const contenido = document.getElementById('con2');
  const iduser = document.getElementById('iduser').innerText;

  axios.get('/api/Dientes', {
    params: {
      iduser: iduser
    }
  })
  .then(function(response) {
    // Manejar respuesta exitosa
    console.log(response.data);
    const data = response.data;

    for (let items in data) {
      const contenidoAdicional = document.createElement('div');
      contenidoAdicional.classList.add('contenido-adicional');

      const contenidoHtml = `
        <tr>
          <td id="ndiente">${data[items].Numero_diente}</td>
          <td id="ediente">-</td>
          <td id="ediente">${data[items].estado_diente}</td>
          <td id="sdiente">${data[items].seccion_diente}</td>
        </tr>
        <br>
      `;

      // Buscar elementos existentes con la misma fecha y descripción
      const elementosExistentes = document.querySelectorAll('.informacion');
      let elementoExistente = null;
      for (let i = 0; i < elementosExistentes.length; i++) {
        const fechaExistente = elementosExistentes[i].querySelector('.fecha');
        const descriptionExistente = elementosExistentes[i].querySelector('.tratamiento');
        if (fechaExistente.textContent === data[items].fecha_registro) {
          elementoExistente = elementosExistentes[i];
          break;
        }
      }

      if (elementoExistente) {
        const contenidoAdicional = elementoExistente.nextElementSibling;
        contenidoAdicional.innerHTML += contenidoHtml;
      } else {
        const detallediente = `
          <div id="contenido" class="observacion">
            <div class="informacion">
              <tr>
                <th scope="col" id="borde" class="borde-inferior">
                  <p id="hfecha" class="fecha">${data[items].fecha_registro}</p>
                </th>
              </tr>
              <span class="expandir" onclick="expandirInformacion(this)">+</span>
            </div>
            <div class="contenido-adicional">
              <!-- Contenido adicional a mostrar al expandir -->
              ${contenidoHtml}
            </div>
          </div>
        `;
        contenido.innerHTML += detallediente;
      }
    }
  })
  .catch(function(error) {
    // Manejar error
    console.log(error);
  })
  .finally(function() {
    // Siempre se ejecutará
    console.log("Ejecución finalizada");
  });
}