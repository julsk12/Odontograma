
(function () {
    'use strict'
    const forms = document.querySelectorAll('.requires-validation')
    Array.from(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
                const nombre_tratamiento = document.getElementById("nombre").value;
                const descripcion = document.getElementById("descripcion").value;
                const duracion = document.getElementById("duracion").value;
                const costo = document.getElementById("costo").value;
                console.log(nombre_tratamiento, descripcion, duracion, costo);

                axios
                    .post(
                        '/api/guardartrat', {
                        nombre_tratamiento: nombre_tratamiento,
                        descripcion: descripcion,
                        duracion: duracion,
                        costo: costo
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
  


/*// Obtén una referencia a la tabla por su ID
const tablaTratamientos = document.getElementById('tabla-tratamientos');

function llenarTabla() {
    axios.get('/api/alltratamientos', {
        responseType: 'json'
    })
    .then(function (response) {
        let datos = response.data;

        // Genera las filas de la tabla con los datos obtenidos
        let filas = '';
        for (let i = 0; i < datos.length; i++) {
            filas += `
                <tr>
                    <td>${datos[i].id}</td>
                    <td>${datos[i].nombre}</td>
                    <td>${datos[i].descripcion}</td>
                    <td>${datos[i].duracion}</td>
                    <td>${datos[i].costo}</td>
                </tr>`;
        }

        // Asigna las filas generadas a la tabla
        tablaTratamientos.querySelector('tbody').innerHTML = filas;

        // Inicializa DataTables en la tabla
        $(tablaTratamientos).DataTable({
            // Aquí puedes especificar las opciones de DataTables
        });
    })
    .catch(function (error) {
        // Maneja los errores aquí
        console.log(error);
    });
}

window.addEventListener('load', llenarTabla);*/