//let table = new DataTable('#example');
// $(document).ready(function() {
//     $('#example').DataTable();
// } );
window.addEventListener('load', function() {
  viewtratamiento();
});
$.noConflict();
jQuery(document).ready(function() {
    jQuery('#example').DataTable();
  });

  function viewtratamiento() {
    let table = $('#tabla-tratamiento').DataTable();
  
    axios.get('/api/mistratamientos', {
      responseType: 'json'
    })
      .then(function (response) {
        let datos = response.data;
  
        if (Array.isArray(datos)) {
          datos.forEach(function (tratamiento) {
            table.row.add([
              tratamiento.id,
              tratamiento.nombre,
              tratamiento.id_odonto,
              tratamiento.fecha_inicio,
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
              tratamiento.nombre_odontologo,
              tratamiento.fecha_creacion,
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
  

  // $(document).ready(function () {
  //   viewtratamiento();
  // });