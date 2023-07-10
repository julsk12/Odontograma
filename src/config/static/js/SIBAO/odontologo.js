function viewodontologo() {
  let table = $('#tabla-odontologos').DataTable();

  axios.get('/api/misodon', {
    responseType: 'json'
  })
    .then(function (response) {
      let datos = response.data;

      if (Array.isArray(datos)) {
        datos.forEach(function (odontologo) {
          table.row.add([
            odontologo.id,
            odontologo.nombre,
            odontologo.fecha_nacimiento,
            odontologo.correo,
            odontologo.costo
          ]).draw(false);
        });
      } else if (typeof datos === 'object') {
        Object.values(datos).forEach(function (odontologo) {
          table.row.add([
            odontologo.id,
            odontologo.nombre,
            odontologo.fecha_nacimiento,
            odontologo.correo,
            odontologo.telefono
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
  viewodontologo();
});

function viewodontologoS() {
  let table = $('#tabla-odonto').DataTable();

  axios.get('/api/misodon', {
    responseType: 'json'
  })
    .then(function (response) {
      let datos = response.data;

      if (Array.isArray(datos)) {
        datos.forEach(function (odontologo) {
          table.row.add([
            odontologo.id,
            odontologo.nombre,
            odontologo.fecha_nacimiento,
            odontologo.correo,
            odontologo.telefono,
            '<button onclick="openModal(this)" class="editar-btn"><i class="fas fa-edit"></i></button>', // Botón de edición con el icono de lápiz
            '<button class="eliminar-btn"><i class="fas fa-trash"></i></button>'
          ]).draw(false);
        });
      } else if (typeof datos === 'object') {
        Object.values(datos).forEach(function (odontologo) {
          table.row.add([
            odontologo.id,
            odontologo.nombre,
            odontologo.fecha_nacimiento,
            odontologo.correo,
            odontologo.telefono,
            '<button onclick="openModal(this)" class="editar-btn"><i class="fas fa-edit"></i></button>', // Botón de edición con el icono de lápiz
            '<button onclick= "eliminarper(this)" class="eliminar-btn"><i class="fas fa-trash"></i></button>'
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
  viewodontologoS();
});

function viewpacienteS() {
  let table = $('#tabla-pacientes').DataTable();

  axios.get('/api/mispac', {
    responseType: 'json'
  })
    .then(function (response) {
      let datos = response.data;

      if (Array.isArray(datos)) {
        datos.forEach(function (odontologo) {
          table.row.add([
            odontologo.id,
            odontologo.nombre,
            odontologo.fecha_nacimiento,
            odontologo.correo,
            odontologo.telefono,
            '<button onclick="openModal(this)" class="editar-btn"><i class="fas fa-edit"></i></button>', // Botón de edición con el icono de lápiz
            '<a onclick= "eliminarper(this)" class="eliminar-btn"><i class="fas fa-trash"></i></a>'
          ]).draw(false);
        });
      } else if (typeof datos === 'object') {
        Object.values(datos).forEach(function (odontologo) {
          table.row.add([
            odontologo.id,
            odontologo.nombre,
            odontologo.fecha_nacimiento,
            odontologo.correo,
            odontologo.telefono,
            '<button onclick="openModal(this)" class="editar-btn" ><i class="fas fa-edit"></i></button>', // Botón de edición con el icono de lápiz
            '<button onclick= "eliminarper(this)" class="eliminar-btn"><i class="fas fa-trash"></i></button>'
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
  viewpacienteS();
});

function viewsecretaria() {
  let table = $('#tabla-secret').DataTable();

  axios.get('/api/misecret', {
    responseType: 'json'
  })
    .then(function (response) {
      let datos = response.data;

      if (Array.isArray(datos)) {
        datos.forEach(function (odontologo) {
          table.row.add([
            odontologo.id,
            odontologo.nombre,
            odontologo.fecha_nacimiento,
            odontologo.correo,
            odontologo.telefono,
            '<a onclick="openModal(this)" class="editar-btn"><i class="fas fa-edit"></i></a>', // Botón de edición con el icono de lápiz
            '<a onclick= "eliminarper(this)" class="eliminar-btn"><i class="fas fa-trash"></i></a>'
          ]).draw(false);
        });
      } else if (typeof datos === 'object') {
        Object.values(datos).forEach(function (odontologo) {
          table.row.add([
            odontologo.id,
            odontologo.nombre,
            odontologo.fecha_nacimiento,
            odontologo.correo,
            odontologo.telefono,
            '<button onclick="openModal(this)" class="editar-btn" ><i class="fas fa-edit"></i></button>', // Botón de edición con el icono de lápiz
            '<button onclick= "eliminarper(this)" class="eliminar-btn"><i class="fas fa-trash"></i></button>'
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
  viewsecretaria();
});

// -------------------------------ELIMINAR----------------------------
function eliminarper(btn) {
  var fila = $(btn).closest('tr'); // Obtener la fila actual utilizando el selector 'tr'
  var id = fila.find('td:first-child').text(); // Obtener el valor de la cédula dentro de la primera celda
  console.log(id);
  axios.delete('/api/eliminarU', {
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
var id;
// Función para abrir el modal
function openModal(btn) {
  var fila = $(btn).closest('tr'); // Obtener la fila actual utilizando el selector 'tr'
  id = fila.find('td:first-child').text(); // Obtener el valor de la cédula dentro de la primera celda y eliminar espacios en blanco
  console.log(id);
  modal.style.display = 'block';

}
//------------------------------ACTUALIZAR-------------------------------------
function alertaa() {
  const idValue = id;
  const name = document.getElementById('nombre').value;
  const telef = document.getElementById('telefono').value;
  const direccion = document.getElementById('direccion').value;
  const correo = document.getElementById('correo').value;
  const contra = document.getElementById('contrasena').value;

  console.log(idValue, name, telef, direccion, correo, contra)
  if (name == "" || telef == "" ||
    direccion == "" || correo == "" || contra == "") {
    Swal.fire({
      title: 'Hay campos vacios!',
      text: 'Por favor complete todos los campos.',
      imageWidth: 400,
      imageHeight: 200,
      imageAlt: 'Custom image',
    })
  } else {
    axios.post('/api/actualizardatos', {
      id: id,
      nombre: name,
      correo: correo,
      telefono: telef,
      direccion: direccion,
      password: contra
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
