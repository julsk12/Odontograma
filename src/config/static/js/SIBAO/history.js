function viewhistory() {
  let morfismo = document.getElementById('container12');
  const busqui = document.getElementById('busqui').value;

  axios.post('/api/head2', {
    id: busqui,
    responseType: 'json'
  })
    .then(function (response) {
      let datos = response.data;
      var length = Object.keys(datos).length + 1;
      let listper = '';

      for (let index = 1; index < length; index++) {
        listper += `<header class="titulo">Historial Clinico</header><br>
            <p class="atri">Nombre: ${datos[index].nombre}</p>
            <p class="atri">Cedula: ${datos[index].id}</p>
            <p class="atri">Correo: ${datos[index].correo}</p>
            <p class="atri">Telefono: ${datos[index].telefono}</p>
            <p class="atri">Direccion: ${datos[index].direccion}</p>
            <p class="atri">Fecha nacimiento: ${datos[index].fecha_nacimiento}</p>
            <p class="atri">Fecha creacion: ${datos[index].fecha_creacion}</p>
            <p class="atri">Tratamientos: ${datos[index].tratamiento}</p>
            <p class="atri">Nombre responsable: ${datos[index].nombre_odontologo}</p>
            <p class="atri">Descripcion: ${datos[index].descripcion}</p>
            <p class="atri">Duracion: ${datos[index].duracion}</p>
            <p class="atri">Diente: ${datos[index].diente}</p>
            <p class="atri">Daño: ${datos[index].tipo_daño}</p><br>`;
      }

      morfismo.innerHTML = listper;
    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}

function genPDF() {
  var doc = new jsPDF();
  var container = document.getElementById('container12');
  doc.fromHTML(container.innerHTML, 15, 15, {
    'width': 170,
  });
  doc.save('saveus.pdf')

}
