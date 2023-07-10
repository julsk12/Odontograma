const tiempoTranscurrido = Date.now();
const hoy = new Date(tiempoTranscurrido);

window.addEventListener('load', function() {
  viewhistory();
});

function viewhistory() {
  let morfismo = document.getElementById('certi');

  axios.get('/api/misdatos', {
    responseType: 'json'
  })
    .then(function (response) {
      let datos = response.data;
      var length = Object.keys(datos).length + 1;
      let listper = '';
      
      for (let index = 1; index < length; index++) {
        listper += `<textarea class="" disabled>
CERTIFICA que el (la) señor(a) ${datos[index].nombre} con documento de identidad C.C ${datos[index].id}, a la fecha de expedición de la
presente comunicación, consta en nuestra base de datos del Régimen Subsidiado en estado Activo(a) en la ciudad de Barranquilla, desde ${datos[index].fecha_registro}.
Recuerde que cuando adquiera nuevamente un vinculo laboral su cobertura en salud le será dada nuevamente por nosotros bajo el Régimen Contributivo.
En Salud Total apreciamos la confianza que usted ha depositado en nosotros y esperamos que usted y su familia continúen disfrutando de nuestros servicios de
salud con Calidad total. Cualquier información adicional, con gusto será atendida por el personal de servicio al cliente de la sede administrativa de su ciudad, o
puede comunicarse con nuestra línea gratuita xxx xxx xxx a nivel nacional o en Bogotá al teléfono xxxxxxx.
Se expide el ${hoy.toDateString()}  atendiendo la solicitud del interesado.

CARTA NO VÁLIDA PARA TRASLADO

Cordialmente,

Gerencia de Operaciones Comercial
                    </textarea>`;
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
  var container = document.getElementById('certi');
  
  // Cambiar el tipo de letra a Times New Roman
  doc.setFont("times", "normal"); // Establecer "times" como tipo de letra
  doc.fromHTML(container.innerHTML, 15, 15, {
    'width': 170,
  });
  
  doc.save('certificado.pdf');
}

// function generatePDF() {
//   // Generar el PDF utilizando los datos obtenidos y mostrados en el contenedor
//   doc.fromHTML(document.getElementById('container12').innerHTML, 15, 15, {
//     'width': 170,
//     'elementHandlers': specialElementHandlers
//   });

//   // Guardar el PDF con el nombre 'document.pdf'
//   doc.save('document.pdf');
// }

// var specialElementHandlers = {
//     '#editor': function (element, renderer) {
//         return true;
//     }
// };

// $('#cmd').click(function () {   

// });