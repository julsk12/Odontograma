function GuardarRegistroPaciente() {
    const cedula = document.getElementById('CedulaPaciente');
    const nombre = document.getElementById('NombreCompletoPaciente');
    const fechaNacimiento = document.getElementById('FechaNacimientoPaciente');
    const correo = document.getElementById('EmailPaciente');
    const password = document.getElementById('ContraseñaPaciente');
    const telefono = document.getElementById('TelefonoPaciente');
    const direccion = document.getElementById('DireccionPaciente');

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

    const passwordValue = password.value.trim();
    if (passwordValue.length < 6) {
        password.classList.add('error');
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'La contraseña debe tener al menos 6 caracteres'
        });
        password.style.border = '1px solid red';
        return;
    } else {
        password.style.border = '1px solid green';
        password.style.border = '1px solid lightblue';
    }

    const telefonoValue = telefono.value.trim();
    const telefonoRegex = /^\d{10}$/;
    if (!telefonoRegex.test(telefonoValue)) {
        telefono.classList.add('error');
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Ingresa un número de teléfono válido (10 dígitos)'
        });
        telefono.style.border = '1px solid red';
        return;
    } else {
        telefono.style.border = '1px solid green';
        telefono.style.border = '1px solid lightblue';
    }

    const direccionValue = direccion.value.trim();
    if (direccionValue.length === 0) {
        direccion.classList.add('error');
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Debes ingresar una dirección'
        });
        direccion.style.border = '1px solid red';
        return;
    } else {
        direccion.style.border = '1px solid green';
        direccion.style.border = '1px solid lightblue';
    }

    const loadingMessage = Swal.fire({
        title: 'Guardando',
        text: 'Por favor, espere...',
        showCancelButton: false,
        showConfirmButton: false,
        allowOutsideClick: false,
        allowEscapeKey: false,
        onBeforeOpen: () => {
            Swal.showLoading();
        }
    });

    // Obtener la dirección IP mediante la función llamada
    getDireccionIP()
        .then((direccionIP) => {
            // Realizar la solicitud POST con la dirección IP obtenida
            axios.post('guardapacientes', {
                fullid: cedulaValue,
                fullname: nombreValue,
                fullfecha_nacimiento: fechaNacimiento.value,
                fullcorreo: correoValue,
                fullpassword: passwordValue,
                fulltelefono: telefonoValue,
                fulldireccion: direccionValue,
                direccion_ip: direccionIP,
                id_roles: 3, // Asignar el valor de id_roles deseado
                roles: {
                    id: 3, // Asignar el valor del ID del rol deseado
                    roles: 'Nombre del Rol' // Asignar el valor del rol deseado
                }
            }, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(function (response) {
                // Manejar todas las respuestas del servidor si es true o false
                if (response.data.error) {
                    // Mostrar un sweet alert si la respuesta del servidor es correcta
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
          .catch(function (error) {
            // Cerrar mensaje de carga
            loadingMessage.close();

            // Mostrar mensaje de error genérico
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Ocurrió un error al guardar el registro. Por favor, intenta nuevamente.'
            });

            // Manejar los errores si el servidor está inactivo por cualquier motivo
            console.log(error);
        });
})
        .catch((error) => {
            console.error(error);
        });
}
function limpiarCampos() {
    document.getElementById('CedulaPaciente').value = '';
    document.getElementById('NombreCompletoPaciente').value = '';
    document.getElementById('FechaNacimientoPaciente').value = '';
    document.getElementById('EmailPaciente').value = '';
    document.getElementById('ContraseñaPaciente').value = '';
    document.getElementById('TelefonoPaciente').value = '';
    document.getElementById('DireccionPaciente').value = '';
  
    // Restauramos los bordes aqui
    const inputs = document.querySelectorAll('input');
    inputs.forEach(input => {
      input.style.border = '1px solid transparent';
    });
  }

function getDireccionIP() {
    // Realizar una solicitud a un servicio de obtención de dirección IP (puede ser un servicio de terceros)
    // En este ejemplo, se utiliza la API de ipify.org
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
  document.getElementById('CedulaPaciente').addEventListener('click', () => {
    document.getElementById('CedulaPaciente').style.border = '1px solid transparent';
  });
  
  document.getElementById('NombreCompletoPaciente').addEventListener('click', () => {
    document.getElementById('NombreCompletoPaciente').style.border = '1px solid transparent';
  });
  
  document.getElementById('FechaNacimientoPaciente').addEventListener('click', () => {
    document.getElementById('FechaNacimientoPaciente').style.border = '1px solid transparent';
  });
  
  document.getElementById('EmailPaciente').addEventListener('click', () => {
    document.getElementById('EmailPaciente').style.border = '1px solid transparent';
  });
  
  document.getElementById('ContraseñaPaciente').addEventListener('click', () => {
    document.getElementById('ContraseñaPaciente').style.border = '1px solid transparent';
  });
  
  document.getElementById('TelefonoPaciente').addEventListener('click', () => {
    document.getElementById('TelefonoPaciente').style.border = '1px solid transparent';
  });
  
  document.getElementById('DireccionPaciente').addEventListener('click', () => {
    document.getElementById('DireccionPaciente').style.border = '1px solid transparent';
  });
