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
