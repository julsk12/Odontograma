
function viewtratamiento() {
  let table = $('#tabla-tratamientos').DataTable();

  axios.get('/api/alltratamientos', {
    responseType: 'json'
  })
    .then(function (response) {
      let datos = response.data;

      if (Array.isArray(datos)) {
        datos.forEach(function (tratamiento) {
          table.row.add([
            tratamiento.id,
            tratamiento.nombre,
            tratamiento.descripcion,
            tratamiento.duracion,
            tratamiento.costo
          ]).draw(false);
        });
      } else if (typeof datos === 'object') {
        Object.values(datos).forEach(function (tratamiento) {
          table.row.add([
            tratamiento.id,
            tratamiento.nombre,
            tratamiento.descripcion,
            tratamiento.duracion,
            tratamiento.costo
          ]).draw(false);
        });
      } else {
        console.log('Los datos recibidos no son válidos.');
      }
    })
    .catch(function (error) {
      console.log(error);
    });
}

$(document).ready(function () {
  viewtratamiento();
});


  function viewtrata() {
    let table = $('#tabla-trata').DataTable();
  
    axios.get('/api/alltratamientos', {
      responseType: 'json'
    })
      .then(function (response) {
        let datos = response.data;
  
        if (Array.isArray(datos)) {
          datos.forEach(function (tratamiento) {
            table.row.add([
              tratamiento.id,
              tratamiento.nombre,
              tratamiento.descripcion,
              tratamiento.duracion,
              tratamiento.costo,
              '<button onclick= "openModal1(this)" class="editar-btn" ><i class="fas fa-edit"></i></button>', // Botón de edición con el icono de lápiz
              '<button onclick= "eliminarper(this)" class="eliminar-btn"><i class="fas fa-trash"></i></button>'
            ]).draw(false);
          });
        } else if (typeof datos === 'object') {
          Object.values(datos).forEach(function (tratamiento) {
            table.row.add([
              tratamiento.id,
              tratamiento.nombre,
              tratamiento.descripcion,
              tratamiento.duracion,
              tratamiento.costo,
              '<button onclick= "openModal1(this)" class="editar-btn" ><i class="fas fa-edit"></i></button>', // Botón de edición con el icono de lápiz
              '<button onclick= "eliminartrata(this)" class="eliminar-btn"><i class="fas fa-trash"></i></button>'
            ]).draw(false);
          });
        } else {
          console.log('Los datos recibidos no son válidos.');
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  
  $(document).ready(function () {
    viewtrata();
  });

  function eliminartrata(btn) {
    var fila = $(btn).closest('tr'); // Obtener la fila actual utilizando el selector 'tr'
    var id = fila.find('td:first-child').text(); // Obtener el valor de la cédula dentro de la primera celda
    console.log(id);
    axios.delete('/api/eliminarT', {
      data: {
        id: id
      }
    })
      .then(function (response) {
        fila.remove(); // Eliminar la fila de la tabla
        console.log(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  //-------------------------------actualizar-------------------------

// Obtén el modal y el botón de cerrar
var modal = document.querySelector('.modal');
var closeBtn = document.querySelector('.close');

// Añade un evento click al botón de cerrar para cerrar el modal
closeBtn.addEventListener('click', function () {
  modal.style.display = 'none';
});

// Añade un evento click a cualquier parte del modal para cerrarlo también
modal.addEventListener('click', function (event) {
  if (event.target === modal) {
    modal.style.display = 'none';
  }
});
var idflex;
// Función para abrir el modal
function openModal1(btn) {
  var fila = $(btn).closest('tr'); // Obtener la fila actual utilizando el selector 'tr'
  idflex = fila.find('td:first-child').text(); // Obtener el valor de la cédula dentro de la primera celda y eliminar espacios en blanco
  console.log(idflex);
  modal.style.display = 'block';

}
function alert2() {
  const idValue = idflex;
  const name = document.getElementById('nombreT').value;
  const descrip = document.getElementById('des').value;
  const duracion = document.getElementById('duracion').value;
  const costo = document.getElementById('costo').value;

  console.log(idValue, name, descrip, duracion, costo)
  if (name == "" || descrip == "" ||
  duracion == "" || costo == "") {
    Swal.fire({
      title: 'Hay campos vacios!',
      text: 'Por favor complete todos los campos.',
      imageAlt: 'Custom image',
    })
  } else {
    axios.post('/api/actualizartratamientos', {
      id: idValue,
      nombre: name,
      descripcion: descrip,
      duracion: duracion,
      costo: costo
    })
    .then((res) => {
      console.log(res.data);
    })
    .catch((err) => {
      console.log(err);
    });
    Swal.fire({
      icon: 'sucess',
      title: 'Good',
      text: 'Los datos se han actualizado con exito',
    })
  }

}

  