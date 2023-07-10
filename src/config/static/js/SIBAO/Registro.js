/*** LOGIN, VERIFICA EL DATO EN LA BAE DE DATOS ***/
function Login() {
  const Email = document.getElementById('CorreoElectronico1');
  const Password = document.getElementById('Contrasena1');
  axios
    .post('login', {
      fullcorreo: Email.value,
      fullpassword: Password.value,
    })
    .then(function (response) {
      const data = response.data;
      if (data.message === 'Tus credenciales han expirado') {
        alert(data.message);
      } else {
        // Las credenciales son válidas, procesar el token, etc.
        const token = data.token;
        const id_roles = data.id_roles;
        console.log(token);
        localStorage.setItem('token', token); // Almacena el token en el LocalStorage
        localStorage.setItem('id_roles', id_roles); // Almacena el id_roles en el LocalStorage

        // Redirigir a la vista correspondiente según el id_roles
        if (id_roles === 1) {
          window.location.href = '/fronted/indexHomeIndexSecretaria';
        } else if (id_roles === 2) {
          window.location.href = '/fronted/indexHomeIndexLight';
        } else {
          // Si el id_roles no coincide con ninguno de los casos anteriores, mostrar un mensaje de error o redirigir a una página de acceso denegado.
          alert('Acceso denegado');
        }
      }
    })
    .catch(function (error) {
      // Si la respuesta del servidor es un error, mostramos un mensaje de error al usuario.
      console.log(error);
      alert('Invalid username or password');
    });
}

//--------------------------------------------------------------------------------------------------------------------------------------
// function checkTokenExpiration() {
//   const token = localStorage.getItem('token');

//   axios.get('checktoken', {
//     headers: {
//       Authorization: `Bearer ${token}`
//     }
//   })
//     .then(function (response) {
//       const data = response.data;
//       if (data.token_expired) {
//         handleTokenExpired();
//       } else {
//         // El token es válido, continuar con el flujo normal de la página
//         // ...
//       }
//     })
//     .catch(function (error) {
//       console.log(error);
//     });

//   console.log('Authorization Header:', `Bearer ${token}`);
// }

// function handleTokenExpired() {
//   const currentPage = window.location.pathname;

//   if (currentPage === 'indexHomeIndexLight') {
//     alert('Tu sesión ha expirado');
//     console.log("Si Pasó aquí");
//     localStorage.removeItem('token');
//     window.location.href = '/login';
//   }
// }

// window.addEventListener('load', function () {
//   checkTokenExpiration();

//   // Verificar el estado del token cada 5 segundos
//   setInterval(checkTokenExpiration, 5000);
// });



//--------------------------------------------------------------------------------------------------------------------------------------



//ESTE ES PARA OCULTAR EL FORMULARIO DE REGISTRO/LOGIN A OLVIDAR CONTRASEÑA//
function ocultarFormulario() {
  var formulario = $('#formulario');
  var formularioNuevo = $('#nuevo-formulario');
  var tiempoEspera = 0;

  // Verificar la velocidad de la conexión del usuario
  if (navigator.connection) {
    switch (navigator.connection.effectiveType) {
      case 'slow-2g':
      case '2g':
      case '3g':
        tiempoEspera = 5000; // Esperar 4 segundos para conexiones lentas
        break;
      case '4g':
      case 'wifi':
        tiempoEspera = 2000; // Esperar 1 segundo para conexiones rápidas
        break;
      case '5g':
      case 'wifi':
        tiempoEspera = 1000; // Esperar 1 segundo para conexiones rápidas
        break;
    }
  }

  $('#pantalla-carga').show();
  formulario.addClass('animate__animated animate__fadeOut');
  setTimeout(function(){
    formulario.hide();
    formulario.removeClass('animate__animated animate__fadeOut');
    formularioNuevo.show();
    $('#pantalla-carga').hide();
  }, tiempoEspera); // Esperar el tiempo determinado antes de mostrar el nuevo formulario
}
//FIN PARA OCULTAR EL FORMULARIO DE REGISTRO/LOGIN A OLVIDAR CONTRASEÑA//

//ESTE ES PARA OCULTRAR REGISTRO DE OLVIDAR CONTRASEÑA A VERIFICACION DE CODE//
function ocultarNuevoFormulario() {
  var formulario = $('#formulario');
  var formularioNuevo = $('#nuevo-formulario');
  var emailIcon = $('.email-icon');
  var errorIcon = $('.error-icon');
  var passedIcon = $('.passed-icon');
  var emailInput = $('#Gmail');
  var text = $('#text1');

  $('#pantalla-carga').show();
  formularioNuevo.addClass('animate__animated animate__fadeOut');

  // Obtener tiempo de carga de la página
  var tiempoCarga = window.performance.timing.domContentLoadedEventEnd - window.performance.timing.navigationStart;
  setTimeout(function(){
    formularioNuevo.hide();
    formularioNuevo.removeClass('animate__animated animate__fadeOut');
    formulario.show();
    $('#pantalla-carga').hide();
    emailInput.val('');
    emailIcon.removeClass('animate__animated animate__shakeX animate__delay-1s');
    errorIcon.hide();
    passedIcon.hide();
    text.text('');
    emailInput[0].setCustomValidity('');
    emailInput[0].value = '';
  }, tiempoCarga); // espera tiempo de carga antes de mostrar el formulario original
}
//ESTE ES PARA OCULTRAR REGISTRO DE OLVIDAR CONTRASEÑA A VERIFICACION DE CODE//

//-------------ESTE ES PARA VERIFICAR EMAIL-------------//
function verificarEmail() {
  const Email = document.getElementById('Gmail');
  var formularioCode = document.getElementById("FormularioCode");
  var formularioNuevo = document.getElementById("nuevo-formulario");

  function mostrarAlerta() {
    Swal.fire({
      title: "Correo enviado",
      text: "Se ha enviado un correo con instrucciones para recuperar la contraseña.",
      icon: "success",
      confirmButtonText: "Aceptar",
      customClass: {
        popup: 'my-custom-class',
      }
    }).then(function(result) {
      formularioCode.style.display = "block";
      formularioNuevo.style.display = "none";
    });
  }

  function mostrarErrorDemasiadasSolicitudes(timeToWait) {
    const hours = Math.floor(timeToWait / 3600);
    const minutes = Math.floor((timeToWait % 3600) / 60);
    const seconds = Math.floor(timeToWait % 60);

    Swal.fire({
      title: "Demasiadas solicitudes",
      text: `Se han realizado demasiadas solicitudes en un período corto de tiempo. Inténtalo de nuevo en ${hours} hora(s), ${minutes} minuto(s), y ${seconds} segundo(s).`,
      icon: "error",
      confirmButtonText: "Reintentar",
      showCloseButton: true, // Agrega la opción showCloseButton para mostrar el botón de cerrar
      customClass: {
        popup: 'my-custom-class',
      }
    }).then(function(result) {
      if (result.isConfirmed) {
        verificarEmail(); // Llamada recursiva
      }
    });
  }

  function mostrarError() {
    Swal.fire({
      title: "Error",
      text: "Se ha producido un error al procesar su solicitud. Inténtalo de nuevo más tarde.",
      icon: "error",
      confirmButtonText: "Aceptar",
      customClass: {
        popup: 'my-custom-class',
      }
    });
  }

  axios.post('forgotpassword', {
    fullcorreo: Email.value,
  })
  .then(function(response) {
    mostrarAlerta();
  })
  .catch(function(error) {
    console.log(error);
    if (error.response.status === 429) {
      const timeToWait = error.response.data.time_to_wait;
      mostrarErrorDemasiadasSolicitudes(timeToWait);
    } else {
      mostrarError();
    }
  });
};



//-------------FIN PARA VERIFICAR EMAIL-------------//

//-------------ESTE ES EL DE VERIFICAR CODE, DEBE CUMPLIR CON UNA NORMATIVA DE 4 DIGITOS Y VALORES NUMÉRICOS----------//
const digitInput = document.querySelector('.digit1');
const verifyButton = document.querySelector('#Verify');

digitInput.addEventListener('input', function(event) {
  const digits = event.target.value;

  if (digits.length === 4 && /^\d+$/.test(digits)) {
    verifyButton.style.display = "block";
  } else {
    verifyButton.style.display = "none";
  }
});
//-------------FIN DE VERIFICAR CODE, DEBE CUMPLIR CON UNA NORMATIVA DE 4 DIGITOS Y VALORES NUMÉRICOS----------//


//INPUT DE OLVIDAR CONTRASEÑA INTELIGENTE
const form = document.querySelector("form"),
  eInput = form.querySelector(".input"),
  text = form.querySelector(".text");
let loadingTimeout;

form.addEventListener("submit", (e) => {
  e.preventDefault(); //preventing form from submitting
  let pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/; //Regex pattern to validate email
  form.classList.add("error");
  form.classList.remove("valid");
  if (eInput.value == "") {
    text.innerText = "Email can't be blank";
  } else if (!eInput.value.match(pattern)) {
    //if pattern is not matched with user's enter value
    text.innerText = "Please enter a valid email";
  } else {
    // Show loading message
    text.innerText = "Loading...";

    // Start a timeout to simulate slow internet
    loadingTimeout = setTimeout(() => {
      // Make the request to the server to verify if the email exists in the database
      axios
        .post("verificarcorreo", {
          fullcorreo: eInput.value,
        })
        .then(function (response) {
          // Clear the loading timeout
          clearTimeout(loadingTimeout);

          // If the server response is successful, the email exists in the database
          form.classList.replace("error", "valid"); //replacing error class with valid class
          text.innerText = "This email exists in the database";
        })
        .catch(function (error) {
          // Clear the loading timeout
          clearTimeout(loadingTimeout);

          // If the server response is an error, the email doesn't exist in the database
          console.log(error);
          form.classList.add("error");
          form.classList.remove("valid");
          text.innerText = "This email doesn't exist in the database";
        });
    }, 2000); // Simulated delay time in milliseconds
  }
});

//FIN //INPUT DE OLVIDAR CONTRASEÑA INTELIGENTE



  //---------------------GUARDAR REGISTRO EN LA BASE DE DATOS--------------------//



  function GuardarRegistro() {
    const cedula = document.getElementById('Cedula');
    const nombre = document.getElementById('Nombre');
    const fechaNacimiento = document.getElementById('fecha');
    const correo = document.getElementById('CorreoElectronicoR');
    const password = document.getElementById('ContrasenaR');
    const telefono = document.getElementById('Telefono');
    const direccion = document.getElementById('Direccion');
    const rol = document.getElementById('rol'); // Obtener el elemento select

  
    const inputs = document.querySelectorAll('input');
    inputs.forEach(input => input.classList.remove('error'));
    inputs.forEach(input => {
      input.style.border = '1px solid transparent'; // Reinicia el borde a transparente
    });
  
    const cedulaValue = cedula.value.trim();
    if (cedulaValue.length !== 10) {
      cedula.classList.add('error');
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'La cédula debe tener 10 dígitos'
      });
      cedula.style.border = '1px solid red';
      return;
    } else {
      cedula.style.border = '1px solid green';
      cedula.style.border = '1px solid lightblue';
    }
  
    const nombreValue = nombre.value.trim();
    if (nombreValue.length <= 10) {
      nombre.classList.add('error');
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'El nombre debe tener más de 10 caracteres'
      });
      nombre.style.border = '1px solid red';
      return;
    } else {
      nombre.style.border = '1px solid green';
      nombre.style.border = '1px solid lightblue';
    }
  
    const fechaValue = new Date(fechaNacimiento.value);
    const currentDate = new Date();
    const eighteenYearsAgo = new Date(
      currentDate.getFullYear() - 18,
      currentDate.getMonth(),
      currentDate.getDate()
    );
  
    if (fechaValue == '0000-00-00' || isNaN(fechaValue.getTime())) {
      fechaNacimiento.classList.add('error');
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'Debes ingresar una fecha de nacimiento válida'
      });
      fechaNacimiento.style.border = '1px solid red';
      return;
    }
  
    if (fechaValue >= eighteenYearsAgo) {
      fechaNacimiento.classList.add('error');
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'Debes ser mayor de 18 años'
      });
      fechaNacimiento.style.border = '1px solid red';
      return;
    }
  
    fechaNacimiento.style.border = '1px solid green';
    fechaNacimiento.style.border = '1px solid lightblue';
  
    const correoValue = correo.value.trim();
    const correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!correoRegex.test(correoValue)) {
      correo.classList.add('error');
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'Ingresa un correo electrónico válido'
      });
      correo.style.border = '1px solid red';
      return;
    } else {
      correo.style.border = '1px solid green';
      correo.style.border = '1px solid lightblue';
    }
  
    const passwordValue = password.value;
    const passwordRegex = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-zA-Z]).{10,}$/;
    if (!passwordRegex.test(passwordValue)) {
      password.classList.add('error');
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'La contraseña debe tener al menos 10 caracteres, incluyendo al menos un número y un carácter especial'
      });
      password.style.border = '1px solid red';
      return;
    } else {
      password.style.border = '1px solid green';
      password.style.border = '1px solid lightblue';
    }
  
    const telefonoValue = telefono.value.trim();
    if (telefonoValue.length !== 10) {
      telefono.classList.add('error');
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'El teléfono debe tener 10 dígitos'
      });
      telefono.style.border = '1px solid red';
      return;
    } else {
      telefono.style.border = '1px solid green';
      telefono.style.border = '1px solid lightblue';
    }
  
    const direccionValue = direccion.value.trim();
    if (!isNaN(direccionValue) || direccionValue === '') {
      direccion.classList.add('error');
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'La dirección debe contener letras y números'
      });
      direccion.style.border = '1px solid red';
      return;
    } else {
      direccion.style.border = '1px solid green';
      direccion.style.border = '1px solid lightblue';
    }
    const rolValue = rol.value; // Obtener el valor seleccionado del select

    if (rolValue === "") {
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'Selecciona un tipo de usuario'
      });
      rol.style.border = '1px solid red';
      return;
    } else {
      rol.style.border = '1px solid green';
      rol.style.border = '1px solid lightblue';
    }
  
  
    // Show loading message
    Swal.fire({
      title: 'Guardando registro...',
      text: 'Espere por favor',
      icon: 'info',
      allowOutsideClick: false,
      showConfirmButton: false,
      onBeforeOpen: () => {
        Swal.showLoading();
      }
    });
  
    getDireccionIP()
      .then((direccionIP) => {
        axios.post('guardaruser', {
            fullid: cedulaValue,
            fullname: nombreValue,
            fullfecha_nacimiento: fechaNacimiento.value,
            fullcorreo: correoValue,
            fullpassword: passwordValue,
            fulltelefono: telefonoValue,
            fulldireccion: direccionValue,
            direccion_ip: direccionIP,
            rol_id: rol.value // Obtener el valor seleccionado del select
          }, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          })
          .then(function(response) {
            if (response.data.error) {
              Swal.fire({
                icon: 'error',
                title: 'Error',
                text: response.data.error
              });
            } else {
              Swal.fire({
                icon: 'success',
                title: 'Éxito',
                text: 'Todos los datos se han guardado correctamente'
              }).then(() => {
                limpiarCampos();
                // document.getElementById('login-register-container').submit();
              });
              console.log(response);
            }
          })
          .catch(function(error) {
            console.log(error);
          });
      })
      .catch((error) => {
        console.error(error);
      });
  }
  function limpiarCampos() {
    document.getElementById('Cedula').value = '';
    document.getElementById('Nombre').value = '';
    document.getElementById('fecha').value = '';
    document.getElementById('CorreoElectronicoR').value = '';
    document.getElementById('ContrasenaR').value = '';
    document.getElementById('Telefono').value = '';
    document.getElementById('Direccion').value = '';
    document.getElementById('rol').value = '';
  
    // Restauramos los bordes aqui
    const inputs = document.querySelectorAll('input');
    inputs.forEach(input => {
      input.style.border = '1px solid transparent';
    });
  }
  
  function getDireccionIP() {
    return axios.get('https://api.ipify.org/?format=json')
      .then((response) => {
        return response.data.ip;
      })
      .catch((error) => {
        console.error(error);
        return null;
      });
  }
  
  // Agrego eventos de escucha para quitar el borde rojo al hacer clic en los campos de entrada
  document.getElementById('Cedula').addEventListener('click', () => {
    document.getElementById('Cedula').style.border = '1px solid transparent';
  });
  
  document.getElementById('Nombre').addEventListener('click', () => {
    document.getElementById('Nombre').style.border = '1px solid transparent';
  });
  
  document.getElementById('fecha').addEventListener('click', () => {
    document.getElementById('fecha').style.border = '1px solid transparent';
  });
  
  document.getElementById('CorreoElectronicoR').addEventListener('click', () => {
    document.getElementById('CorreoElectronicoR').style.border = '1px solid transparent';
  });
  
  document.getElementById('ContrasenaR').addEventListener('click', () => {
    document.getElementById('ContrasenaR').style.border = '1px solid transparent';
  });
  
  document.getElementById('Telefono').addEventListener('click', () => {
    document.getElementById('Telefono').style.border = '1px solid transparent';
  });
  
  document.getElementById('Direccion').addEventListener('click', () => {
    document.getElementById('Direccion').style.border = '1px solid transparent';
  });
  

  //---------------------FIN DE GUARDAR REGISTRO EN LA BASE DE DATOS--------------------//

//---------------VALIDO EL CÓDIGO QUE SE ENVIÓ AL GMAIL--------------//

function sendEmail() {
  // Obtengo algunos datos necesario para el formulario y el correo electrónico del usuario
  const form = document.getElementById('email-form');
  const email = document.getElementById('email-input').value;

  // Creao un objeto FormData con los datos del formulario
  const formData = new FormData(form);

  // Agrego el correo electrónico del usuario a los datos del formulario
  formData.append('email_address', email);

  // Realizao  una petición POST usando metodo fetch al servidor para enviar el correo electrónico
  fetch('send_email', {
    email_address: email.value,
    method: 'POST',
    body: formData,
  })
    .then(response => {
      if (response.ok) {
        Swal.fire({
          icon: 'success',
          title: 'Correo electrónico enviado',
          text: 'El correo electrónico se envió correctamente.',
          animation: true,
          showConfirmButton: false,
          timer: 3000
        });
      } else {
        Swal.fire({
          icon: 'error',
          title: 'Error al enviar',
          text: 'Error al enviar el correo electrónico.',
          animation: true,
          showConfirmButton: false,
          timer: 3000
        });
      }
    })
    .catch(error => {
      console.error(error);
      Swal.fire({
        icon: 'error',
        title: 'Error al enviar',
        text: 'Error al enviar el correo electrónico.',
        animation: true,
        showConfirmButton: false,
        timer: 3000
      });
    });
}
function Verificar() {
  const digit1 = document.querySelector('.digit1');
  const gmailInput = document.getElementById('Gmail');
  const email = gmailInput.value;

  // Show loading message
  Swal.fire({
    title: 'Verificando código...',
    text: 'Espere por favor',
    icon: 'info',
    allowOutsideClick: false,
    showConfirmButton: false,
    onBeforeOpen: () => {
      Swal.showLoading();
    }
  });

  // Start a timeout to simulate slow internet
  const loadingTimeout = setTimeout(() => {
    axios
      .post('verificarcode', {
        verification_code: digit1.value,
      })
      .then(function(response) {
        // Clear the loading timeout
        clearTimeout(loadingTimeout);

        Swal.fire({
          title: 'Verificación exitosa',
          text: 'Se ha verificado correctamente su código.',
          icon: 'success',
          confirmButtonText: 'Aceptar'
        }).then(function() {
          // Asigno algun valor de email al input del segundo formulario
          document.getElementById('EmailActualizacion').value = email;

          // Aqui muestro el segundo formulario
          document.getElementById('modal').style.display = 'block';
        });
      })
      .catch(function(error) {
        // Clear the loading timeout
        clearTimeout(loadingTimeout);

        console.log(error);
        Swal.fire({
          title: 'Verificación fallida',
          text: 'No se ha podido verificar su código.',
          icon: 'error',
          confirmButtonText: 'Aceptar',
          customClass: {
            popup: 'my-custom-class',
          },
        }).then(function() {
          Swal.fire({
            title: 'Acción adicional',
            text: 'Se ha realizado una acción adicional en caso de verificación fallida.',
            icon: 'info',
            confirmButtonText: 'Aceptar'
          });
        });
      });
  }, 2000); // Simulated delay time in milliseconds
}

// function mostrarMensaje() {
//   document.getElementById("tooltipText").style.visibility = "visible";
// }

// function ocultarMensaje() {
//   document.getElementById("tooltipText").style.visibility = "hidden";
// }
//---------------FIN DEL VALIDO EL CÓDIGO QUE SE ENVIÓ AL GMAIL--------------//

//---------------CAMBIO LA CONTRASEÑA A TRAVÉS DEL GMAIL DEL USUARIO----///
function actualizarContrasena() {
  const email = document.getElementById('EmailActualizacion');
  const nuevaContrasena = document.getElementById('NuevaContrasena');

  axios.post('actualizar_contrasena', {
    email: email.value,
    nueva_contrasena: nuevaContrasena.value,
  })
  .then(function(response) {
    // Respuesta satisfacoria para la contraseña
    console.log(response.data);
    Swal.fire({
      title: 'Verificación exitosa',
      text: 'Contraseña actualizada correctamente',
      icon: 'success',
      customClass: {
        popup: 'my-custom-class',
      },
    })
  })
  .catch(function(error) {
    // Ha habido un problema con algo
    console.error(error);
  });
}
function mostrarMensaje() {
  const emailInput = document.getElementById('EmailActualizacion');
  const email = emailInput.value;

  axios.post('obtener_datos', {
    fullemail: email
  })
  .then(function(response) {
    const datos = response.data;
    const tooltipText = document.getElementById("tooltipText");
      
    if (datos) {
      tooltipText.innerHTML = `<strong>Tus datos...?</strong><br>Nombre: ${datos.NombreCompleto}<br>Rol: ${datos.Rol}`;
    } else {
      tooltipText.textContent = 'Correo electrónico no encontrado';
    }
      
    tooltipText.style.visibility = "visible";
  })
  .catch(function(error) {
    console.log(error);
    // Manejao cualuiqe tipo de error en caso de que la solicitud falle
  });
}

function ocultarMensaje() {
  const tooltipText = document.getElementById("tooltipText");
  tooltipText.style.visibility = "hidden";
  tooltipText.textContent = '';
}
//--------------------------------------------------------------------------------------------------


function gestionarRecordarContraseña() {
  const checkbox = document.getElementById('recordarContraseña');
  const isChecked = checkbox.checked;
  const correoValue = document.getElementById('CorreoElectronico1').value;
  const contraseñaValue = document.getElementById('Contrasena1').value;

  if (isChecked && correoValue && contraseñaValue) {
    // Codificar los datos en Base64 antes de guardarlos en el localStorage
    const encodedCorreo = btoa(correoValue);
    const encodedContraseña = btoa(contraseñaValue);

    localStorage.setItem('correoElectronico', encodedCorreo);
    localStorage.setItem('contraseña', encodedContraseña);
  } else {
    localStorage.removeItem('correoElectronico');
    localStorage.removeItem('contraseña');
  }
}

function cargarDatosGuardados() {
  const encodedCorreo = localStorage.getItem('correoElectronico');
  const encodedContraseña = localStorage.getItem('contraseña');

  if (encodedCorreo && encodedContraseña) {
    // Decodificar los datos desde Base64 antes de cargarlos en los campos
    const correoValue = atob(encodedCorreo);
    const contraseñaValue = atob(encodedContraseña);

    document.getElementById('CorreoElectronico1').value = correoValue;
    document.getElementById('Contrasena1').value = contraseñaValue;
    document.getElementById('recordarContraseña').checked = true;
  }
}

document.getElementById('recordarContraseña').addEventListener('change', gestionarRecordarContraseña);

cargarDatosGuardados();


//------------------------------------------------------------------------------------------------